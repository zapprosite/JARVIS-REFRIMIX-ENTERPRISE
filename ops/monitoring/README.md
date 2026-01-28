# Monitoring Infrastructure

This directory contains resources for monitoring the JARVIS RAG System.

## Grafana Dashboard

`grafana_dashboard.json` contains a pre-configured dashboard for "RAG Assurance".

### Metrics Tracked
- **RAG Response Confidence**: Tracks the rate of `low_confidence` vs `success` responses based on structured logs.
- **Source**: Expects logs to be ingested via Promtail/Loki with the label `app="orchestrator"`.

### Importing
1. Open Grafana.
2. Go to **Dashboards** > **New** > **Import**.
3. Copy the content of `grafana_dashboard.json`.
4. Select your Loki datasource.

## Logging Structure
The application emits JSON logs with the following keys for critical events:
- `event_type`: "rag_validation"
- `status`: "success" | "low_confidence" | "error"
- `citation_count`: Number of citations used.
