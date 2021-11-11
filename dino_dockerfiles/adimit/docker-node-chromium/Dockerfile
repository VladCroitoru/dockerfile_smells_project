FROM node:8
MAINTAINER Aleksandar Dimitrov <a.dimitrov@seidemann-web.com>

ENV FF_VERSION="59.0.1"

RUN apt-get update \
 && apt-get install -y chromium ttf-freefont \
 && rm -rf /var/lib/apt/lists/*

RUN apt-get update \
 && apt-get install -y libx11-xcb1 libdbus-glib-1-2 libgtk-3-0 \
 && wget -O FirefoxSetup.tar.bz2 "https://download.mozilla.org/?product=firefox-${FF_VERSION}&os=linux64&lang=en-US" \
 && tar xf /FirefoxSetup.tar.bz2 \
 && ln -s /firefox/firefox /usr/local/bin \
 && rm -f /FirefoxSetup.tar.bz2 \
 && rm -rf /var/lib/apt/lists/* 

USER node

CMD ["node"]
