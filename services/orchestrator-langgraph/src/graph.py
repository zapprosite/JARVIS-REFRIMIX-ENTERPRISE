import os
from typing import Annotated, TypedDict, List
import operator
from langchain_core.messages import BaseMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.postgres import PostgresSaver
from psycopg_pool import ConnectionPool
from src.tools import query_hvac_manuals, search_web

# Environment for LiteLLM
LITELLM_URL = os.getenv("LITELLM_URL", "http://litellm:4000")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "sk-dummy") # LiteLLM usually accepts any key

# Tools
tools = [query_hvac_manuals, search_web]

# Model
# Model
if os.getenv("MOCK_LLM") == "true":
    from langchain_community.chat_models import FakeListChatModel
    # Basic Mock that cycles through responses
    model = FakeListChatModel(responses=[
        "Hello! I am running in Credentialless Mock Mode. How can I help you?",
        "I can help you with HVAC manuals (Simulated).",
        "Error E7 usually means fan lock (Mocked Answer)."
    ])
else:
    model = ChatOpenAI(
        base_url=LITELLM_URL, 
        api_key=OPENAI_API_KEY, 
        model="gpt-4o", # Model name routed by LiteLLM
        temperature=0
    ).bind_tools(tools)

# State
class AgentState(TypedDict):
    messages: Annotated[List[BaseMessage], operator.add]
    tenant_id: str
    user_id: str

# Nodes
def agent_node(state: AgentState):
    messages = state["messages"]
    # We could add system prompt injection here based on tenant_id
    if not any(isinstance(m, SystemMessage) for m in messages):
        sys_msg = SystemMessage(content="You are a helpful HVAC assistant. ALWAYS use the query_hvac_manuals tool for technical questions. Do not guess.")
        messages = [sys_msg] + messages
        
    response = model.invoke(messages)
    return {"messages": [response]}

# Graph
workflow = StateGraph(AgentState)

workflow.add_node("agent", agent_node)
workflow.add_node("tools", ToolNode(tools))

workflow.set_entry_point("agent")

workflow.add_conditional_edges(
    "agent",
    tools_condition,
)
workflow.add_edge("tools", "agent")

# Postgres Persistence
POSTGRES_URL = os.getenv("POSTGRES_URL", "postgresql://user:password@postgres:5432/zappro")

# Conditional Checkpointer for Testing
if os.getenv("TEST_MODE"):
    from langgraph.checkpoint.memory import MemorySaver
    checkpointer = MemorySaver()
else:
    pool = ConnectionPool(conninfo=POSTGRES_URL, max_size=10, timeout=30)
    checkpointer = PostgresSaver(pool)

app = workflow.compile(checkpointer=checkpointer)
