FROM ruby:2.5.1-alpine

RUN apk update && \
    apk add \
    mysql-client mysql-dev \
    nodejs \
    git less \
    imagemagick imagemagick-dev \
    tzdata \
    build-base \
    libxml2 libxml2-dev \
    libxslt libxslt-dev && \
    rm -fr /var/cache/apk/*

RUN ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime
