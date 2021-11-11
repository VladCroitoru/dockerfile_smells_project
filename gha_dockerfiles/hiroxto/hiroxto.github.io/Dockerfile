FROM node:16.10-slim

WORKDIR /app

EXPOSE 8080

RUN apt update -y && \
    apt install -y tzdata

COPY . /app

RUN yarn install

USER node
