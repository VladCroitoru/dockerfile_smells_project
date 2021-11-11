FROM ubuntu:trusty

RUN apt-get update && apt-get install -y apt-transport-https && \
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys FB0ACEBA8887F477 && \
    echo "deb https://spotify.github.io/helios-apt helios main" >> /etc/apt/sources.list && \
    apt-get update && apt-get install -y helios

