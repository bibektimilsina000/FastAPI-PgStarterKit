FROM python:3.11-slim

WORKDIR /app
ENV PYTHONPATH=/app


COPY . /app

RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 80

ENV UVICORN_HOST=0.0.0.0 UVICORN_PORT=80 UVICORN_LOG_LEVEL=info



