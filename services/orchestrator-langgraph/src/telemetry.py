from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource
from openinference.instrumentation.langchain import LangChainInstrumentor
import os

def setup_telemetry(service_name: str = "orchestrator-langgraph"):
    """
    Configures OpenTelemetry for the service.
    """
    if os.getenv("ENABLE_OTEL", "false").lower() != "true":
        return

    resource = Resource.create(attributes={
        "service.name": service_name
    })

    provider = TracerProvider(resource=resource)
    
    # Exporter Configuration
    otlp_endpoint = os.getenv("OTEL_EXPORTER_OTLP_ENDPOINT")
    if otlp_endpoint:
        processor = BatchSpanProcessor(OTLPSpanExporter(endpoint=otlp_endpoint, insecure=True))
    else:
        # Fallback to Console for debug if no endpoint, or do nothing
        # Using ConsoleExporter might spam logs.
        if os.getenv("OTEL_DEBUG") == "true":
             processor = BatchSpanProcessor(ConsoleSpanExporter())
        else:
             return # setup provider but no exporter?

    provider.add_span_processor(processor)
    trace.set_tracer_provider(provider)
    
    # Auto-instrument LangChain
    LangChainInstrumentor().instrument(tracer_provider=provider)
    
    return provider
