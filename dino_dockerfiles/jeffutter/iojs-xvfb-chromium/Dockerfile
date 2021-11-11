FROM iojs:1.6
MAINTAINER jeff@jeffutter.com

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ENV CHROME_BIN /chromium.sh
ENV DISPLAY :99

RUN apt-get update \
    && apt-get install -y xvfb chromium \
    && rm -rf /var/lib/apt/lists/*

COPY chromium.sh /chromium.sh
