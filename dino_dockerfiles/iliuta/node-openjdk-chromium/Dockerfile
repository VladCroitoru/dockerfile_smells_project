FROM node:10-alpine

RUN apk add --no-cache \
    curl \
    python \
    build-base \
    git \
    bash \
    openjdk8-jre-base \
    # chromium dependencies
    udev \
    ttf-freefont \
    chromium-chromedriver \
    chromium

ENV CHROME_BIN /usr/bin/chromium-browser

