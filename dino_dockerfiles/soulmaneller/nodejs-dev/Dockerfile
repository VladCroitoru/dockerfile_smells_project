# This Dockerfile for building a nodejs-runtime image
FROM ubuntu:14.04
MAINTAINER Soulmaneller

ENV LANG C.UTF-8
ENV HOME /root

# ENV NODE_VERSION v0.10

ADD install.sh /opt/
WORKDIR /root

RUN apt-get update; apt-get install -y \
    wget \
    git

RUN wget -qO- https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash

RUN chmod a+x /opt/install.sh; \
    bash -c 'NODE_VERSION=v0.10 /opt/install.sh'

ENTRYPOINT ["/opt/install.sh"]

CMD bash
