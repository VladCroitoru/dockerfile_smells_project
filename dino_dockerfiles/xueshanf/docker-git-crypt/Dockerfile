FROM alpine:edge
MAINTAINER Xueshan Feng <xueshan.feng@gmail.com>

ENV VERSION 0.6.0

RUN apk --update add \
   bash \
   curl \
   git \
   g++ \
   make \
   openssh \
   openssl \
   openssl-dev \
   && rm -rf /var/cache/apk/*

RUN curl -L https://github.com/AGWA/git-crypt/archive/$VERSION.tar.gz | tar zxv -C /var/tmp
RUN cd /var/tmp/git-crypt-$VERSION && make && make install PREFIX=/usr/local

WORKDIR /repo
VOLUME /repo
CMD ["/bin/bash"]
