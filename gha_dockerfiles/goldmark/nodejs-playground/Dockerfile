FROM node:latest

RUN apt-get update \
  && apt-get upgrade -y \
  && rm -rf /var/lib/apt/lists/*

COPY ./app /app

WORKDIR /app

RUN npm install --production
