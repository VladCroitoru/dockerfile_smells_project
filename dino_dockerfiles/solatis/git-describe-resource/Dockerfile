FROM alpine

RUN apk add --no-cache \
  bash \
  git \
  openssh-client \
  ca-certificates \
  jq

RUN ln -s /usr/bin/gpg2 /usr/bin/gpg

ADD assets/ /opt/resource/
RUN chmod +x /opt/resource/*
