FROM debian:wheezy

MAINTAINER David Wisner dwisner6@gmail.com

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    python \
    curl \
    ca-certificates \
    pkg-config \
  && rm -rf /var/lib/apt/lists/*
