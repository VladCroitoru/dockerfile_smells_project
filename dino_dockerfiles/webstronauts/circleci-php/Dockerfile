FROM webstronauts/php

MAINTAINER robin@webstronauts.co

# The dockerize version to install
ENV DOCKERIZE_VERSION v0.6.0

# Add dockerize utilities
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz
