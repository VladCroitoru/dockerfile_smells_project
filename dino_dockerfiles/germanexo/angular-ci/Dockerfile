FROM debian:latest
MAINTAINER ximenag@exo.com.ar

ENV DEBIAN_FRONTEND=noninteractive

# Install basics
RUN apt-get update &&  \
    apt-get install -y git wget curl unzip ruby ruby-dev build-essential xvfb

RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - && \
    apt-get update &&  \
    apt-get install -y nodejs

RUN gem install sass scss_lint

RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    dpkg --unpack google-chrome-stable_current_amd64.deb && \
    apt-get install -f -y && \
    apt-get clean && \
    rm google-chrome-stable_current_amd64.deb

RUN mkdir sources

RUN apt-get clean && \
    apt-get autoclean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR sources
