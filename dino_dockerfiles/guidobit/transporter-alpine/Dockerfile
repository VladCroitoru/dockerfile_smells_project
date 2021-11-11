FROM golang:alpine
MAINTAINER Guido Baars <guido@bit-students.com>

ENV TRANSPORTER_VERSION 0.3.1 
ENV TRANSPORTER_ARCH linux-amd64
ENV TRANSPORTER_TAG transporter-${TRANSPORTER_VERSION}-${TRANSPORTER_ARCH} 

RUN apk add --update curl && \
rm -rf /var/cache/apk/*

RUN curl -L https://github.com/compose/transporter/releases/download/v${TRANSPORTER_VERSION}/${TRANSPORTER_TAG} > /usr/local/bin/transporter && \
  chmod +x /usr/local/bin/transporter

ENTRYPOINT [ "/bin/sh" ]
