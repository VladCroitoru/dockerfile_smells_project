FROM ubuntu:14.04
MAINTAINER Viet Hung Nguyen <hvn@familug.org>

RUN apt-get -y update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*
RUN curl -L https://bootstrap.saltstack.com -o install_salt.sh
# do not (-X install daemon and -d test daemon running)
RUN sh install_salt.sh -P -X -d && rm -rf /var/lib/apt/lists/*

RUN salt-call --versions-report
