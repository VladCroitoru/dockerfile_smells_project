FROM node:latest

RUN apt-get update && apt-get install -y \
    python2.7 \
    git-all \
    pkg-config \
    libncurses5-dev \
    libssl-dev \
    libnss3-dev \
    libexpat-dev \
  && rm -rf /var/lib/apt/lists/*
