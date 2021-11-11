FROM debian:buster-slim

RUN \
  DEBIAN_FRONTEND=noninteractive \
    apt update && apt install --assume-yes --no-install-recommends \
      build-essential \
      nasm \
      vim-common \
      curl \
      wget \
      git \
      docker.io \
  \
  && rm -rf /var/lib/apt/lists/*
