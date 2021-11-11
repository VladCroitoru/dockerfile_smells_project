FROM node:4

RUN apt-get update && apt-get install -y \
  nano

COPY . /root/docker-runner
WORKDIR /root/docker-runner

RUN npm install
