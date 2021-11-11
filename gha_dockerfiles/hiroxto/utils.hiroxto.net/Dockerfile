FROM node:14.17.6-slim

WORKDIR /app

ENV HOST "0.0.0.0"

RUN apt update -y && \
    apt install -y --no-install-recommends tzdata g++ make python && \
    apt-get clean && \
    rm -rf /var/lib/opt/lists/*

COPY . /app

RUN yarn install

EXPOSE 8080
