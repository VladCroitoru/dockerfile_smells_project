FROM golang:latest

RUN apt-get update && apt-get install -y --no-install-recommends \
    libssl-dev libclamav-dev libmagic-dev libyara-dev liblzma-dev \
    && rm -rf /var/lib/apt/lists/*
