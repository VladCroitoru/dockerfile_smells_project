FROM ubuntu:14.04

RUN apt-get update && \
    apt-get upgrade -y

RUN apt-get install -y --no-install-recommends \
    ssh \
    python \
    python-pip \
    curl \
    ca-certificates \
    wget \
    git \
    zip

RUN pip install awscli
