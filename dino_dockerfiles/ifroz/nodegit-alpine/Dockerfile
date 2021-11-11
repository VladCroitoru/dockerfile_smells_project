FROM node:alpine

WORKDIR /srv

RUN apk update && \
    apk upgrade && \
    apk add git libgit2-dev && \
    apk add python tzdata pkgconfig build-base && \
    BUILD_ONLY=true yarn global add nodegit

RUN apk del python tzdata pkgconfig build-base && \
    rm -rf /tmp/* /var/cache/apk/*
