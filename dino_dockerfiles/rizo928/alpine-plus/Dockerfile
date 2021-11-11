#
# Alpine linux docker image
#
# A minimal base image based on Alpine Linux with useful packages and tools.
#
# gliderlabs/alpine has improved packages not avail with the official alpine:latest - e.g. php-apache2, etc.
#

# FROM gliderlabs/alpine
FROM alpine:edge

MAINTAINER Jerald Watts <cysix928@gmail.com>

# Set environment variables.
ENV \
  TERM=xterm-color

# Install packages.
RUN \
  apk add --update --no-cache bash \
    coreutils \
    curl \
    nano \
    vim \
    git \
    tar \
    wget \
    && rm -rf /var/cache/apk/*
    
ADD init.sh /init.sh
RUN chown root:root /init.sh \
    && chmod 755 /init.sh

ENTRYPOINT ["/init.sh"]
