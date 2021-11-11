FROM python:3.9.6-slim

ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y libpq-dev gcc

WORKDIR /src
COPY ./src ./

RUN pip install --upgrade pip && \
    pip install poetry==1.1.10 && \
    poetry config virtualenvs.in-project true && \
    poetry install --no-dev

RUN groupadd -r rss_uviconr && \
    useradd -r -g rss_uviconr rss_uviconr

USER rss_uviconr
WORKDIR /src
COPY entrypoint-app.sh ./

EXPOSE 8020
