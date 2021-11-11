FROM ubuntu:16.04

MAINTAINER "Guy Huynh"

RUN apt-get update \
    && apt-get install --yes \
    python-pip \
    jq \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common \
    php7.0 -y \
    && curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add - \

    && add-apt-repository \
    "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
    $(lsb_release -cs) \
    stable" \

    && apt-get update \
    && apt-get install --yes docker-ce \


    && systemctl enable docker \

    && curl -L https://github.com/docker/compose/releases/download/1.12.0/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose \
    && chmod +x /usr/local/bin/docker-compose \
    && pip install --upgrade pip \
    && pip install --upgrade awscli
