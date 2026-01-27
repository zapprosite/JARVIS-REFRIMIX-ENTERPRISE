import os
from typing import List
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, VectorParams, Distance
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import pypdf
import io
import uuid

# Configuration
QDRANT_URL = os.getenv("QDRANT_URL", "http://qdrant:6333")
COLLECTION_NAME = "manuals"
MODEL_NAME = "all-MiniLM-L6-v2" # Lightweight, good for local/CPU

# Global instances
client = QdrantClient(url=QDRANT_URL)
model = SentenceTransformer(MODEL_NAME)

def init_collection():
    if not client.collection_exists(COLLECTION_NAME):
        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(size=384, distance=Distance.COSINE),
        )

def process_pdf(file_content: bytes, filename: str, tenant_id: str = "public") -> int:
    """
    Parses PDF, chunks it, embeds it, and saves to Qdrant.
    Returns number of chunks ingested.
    """
    init_collection()
    
    # Parse PDF from bytes
    pdf_reader = pypdf.PdfReader(io.BytesIO(file_content))
    text_chunks = []
    
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    
    for page_num, page in enumerate(pdf_reader.pages):
        text = page.extract_text()
        if not text:
            continue
            
        chunks = splitter.split_text(text)
        for chunk in chunks:
            text_chunks.append({
                "text": chunk,
                "metadata": {
                    "filename": filename,
                    "page": page_num + 1,
                    "tenant_id": tenant_id
                }
            })
            
    if not text_chunks:
        return 0
        
    # Embed
    texts = [c["text"] for c in text_chunks]
    embeddings = model.encode(texts).tolist()
    
    # Upsert
    points = []
    for i, chunk in enumerate(text_chunks):
        # Deterministic ID based on content to avoid duplicates? 
        # Or random. Let's use random for now but ideally hash.
        point_id = str(uuid.uuid5(uuid.NAMESPACE_DNS, chunk["text"] + filename))
        
        points.append(PointStruct(
            id=point_id,
            vector=embeddings[i],
            payload={
                "text": chunk["text"],
                **chunk["metadata"]
            }
        ))
        
    # Batch upsert
    client.upsert(
        collection_name=COLLECTION_NAME,
        points=points
    )
    
    return len(points)
