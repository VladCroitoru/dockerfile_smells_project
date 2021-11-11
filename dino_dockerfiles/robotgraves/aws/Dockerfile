FROM ubuntu:16.04

RUN apt-get update
RUN apt-get -y install ansible \
    git \
    bash \
    curl \
    python \
    unzip \
    python-pip \
    jq
RUN pip install docker-compose \
    --upgrade awscli \
    --upgrade ansible

ADD https://releases.hashicorp.com/packer/1.2.3/packer_1.2.3_linux_amd64.zip /tmp/packer.zip
RUN unzip /tmp/packer.zip -d /usr/local/bin
RUN rm /tmp/packer.zip
RUN packer -v
