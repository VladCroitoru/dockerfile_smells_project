FROM ruby:2.5-alpine

LABEL maintainer="Rianol Jou <rianoljou@kkbox.com>"

COPY . /app

WORKDIR /app

RUN apk update &&\
    apk upgrade &&\
    apk add build-base &&\
    bundle install &&\
    rm -rf /tmp/*

EXPOSE 9413

ENTRYPOINT ["puma", "-p", "9413"]
