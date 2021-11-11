FROM ubuntu:16.04
MAINTAINER Krzysztof Suszynski <krzysztof.suszynski@wavesoftware.pl>
RUN apt-get update -q && apt-get install -y \
  curl \
  xvfb \
  git \
  libxss1 \
  libappindicator1 \
  libindicator7 \
  maven \
  openjdk-8-jdk  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -
RUN curl -o google-chrome-stable_current_amd64.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb || apt-get install -f -y
RUN apt-get purge curl -y
RUN apt-get autoremove --purge
RUN rm -rf /var/lib/apt/lists/*
