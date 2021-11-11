FROM openjdk:16-jdk-buster

RUN apt-get update && apt-get install -y \
  wget \
  nodejs \
  git \
  npm \
  jq \
  gettext-base \
  bc \
  && rm -rf /var/lib/apt/lists/*

RUN npm install -g csvtojson