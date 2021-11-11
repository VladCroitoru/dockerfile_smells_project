FROM node:10.15.3-alpine

RUN set -x && \
    apk --update add --no-cache \
      ca-certificates \
      bash \
      openjdk8 \
      git \
      libc6-compat \
      openssh-client  \
      openssl-dev  \
      libssh2  \
      alpine-sdk  \
      python  \
      curl  \
      libcurl  \
      curl-dev && \
    update-ca-certificates && \
    ln -s /usr/lib/libcurl.so.4 /usr/lib/libcurl-gnutls.so.4
