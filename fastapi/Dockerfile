FROM python:3.8.5-slim

WORKDIR /api
COPY . /api

RUN apt-get update -y \
    && apt-get install -y gcc libpq-dev \
    && rm -rf /var/lib/apt/lists/* \
    && pip install -r requirements.txt

EXPOSE 8080

CMD uvicorn --host 0.0.0.0 --port 8080 app:app --reload