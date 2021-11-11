FROM node:8.9-slim

RUN apt-get update && \
  apt-get install -y --no-install-recommends git mysql-client openssh-client \
          libpng-dev && \
  npm i -g yarn lerna && \
  rm -rf /var/lib/apt/lists/*
