FROM python:3-alpine

RUN mkdir -p /app
WORKDIR /app

ENV PYTHONUNBUFFERED 1
COPY requirements.txt requirements-dev.txt /app/
RUN apk update && \
    apk add postgresql-dev gcc musl-dev && \
    pip install -r requirements.txt -r requirements-dev.txt && \
    apk del gcc musl-dev && \
    rm -rf /var/cache/apk/*

COPY . /app

CMD ["python", "src/main.py"]
