FROM python:3.11-slim

WORKDIR /app

# Dependencies
RUN pip install schedule requests

COPY src/ /app/src/

CMD ["python", "src/main.py"]
