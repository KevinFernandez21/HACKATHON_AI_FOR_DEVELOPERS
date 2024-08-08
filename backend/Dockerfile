# Build stage
FROM python:3.10-slim AS builder

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

# Final stage
FROM python:3.10-slim

WORKDIR /app
COPY --from=builder /app .

ENV PYTHONUNBUFFERED True

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app.main:app