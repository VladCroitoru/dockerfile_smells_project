FROM williamyeh/ansible:debian8
MAINTAINER aojea <antonio.ojea.garcia@gmail.com>

ENV DEBIAN_FRONTEND=noninteractive 
  
# Install packages and clear APT cache
# See https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/
RUN apt-get update -qq && apt-get install -yqq --no-install-recommends \
    git \
    sudo \
    curl \
    wget \
    python-pip && \            
    rm -rf /var/lib/apt/lists/*
    
RUN pip install pytest
