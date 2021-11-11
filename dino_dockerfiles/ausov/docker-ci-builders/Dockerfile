FROM ubuntu:latest

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get dist-upgrade -y \
  && apt-get install -y git git-core wget curl zip unzip nano build-essential xvfb
