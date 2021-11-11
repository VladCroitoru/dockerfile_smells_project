FROM alpine:3.7
MAINTAINER Karel Bemelmans <mail@karelbemelmans.com>

# Install packages needed to build
RUN apk add --update --no-cache \
    bash \
    ca-certificates \
    curl \
    python3 \
    wget \
  && pip3 install --upgrade pip \
  && pip3 install -U awscli

# Install hugo.
ARG HUGO_VERSION=0.56.1
ARG HUGO_SHA256=a02bba8e9391008e4d773bbd09e9f11a35f00d599b668e388ae0857dbef48a54

# Rember sha256sum (and md5sum) expect 2 spaces in front of the filename on alpine...
RUN curl -Ls https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_${HUGO_VERSION}_Linux-64bit.tar.gz \
       -o /tmp/hugo.tar.gz \
  && echo "${HUGO_SHA256}  /tmp/hugo.tar.gz" | sha256sum -c - \
  && tar xf /tmp/hugo.tar.gz -C /tmp \
  && mv /tmp/hugo /usr/bin/hugo \
  && rm -rf /tmp/hugo* \
