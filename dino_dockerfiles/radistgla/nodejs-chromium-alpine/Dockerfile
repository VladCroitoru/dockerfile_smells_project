FROM node:8.9.1-alpine as builder

RUN echo "http://dl-4.alpinelinux.org/alpine/v3.4/main" >> /etc/apk/repositories && \
	  echo "http://dl-4.alpinelinux.org/alpine/v3.4/community" >> /etc/apk/repositories

RUN apk update -qq && \
	  apk add -qq curl unzip libexif udev chromium xvfb ttf-freefont

ENV CHROME_BIN=/usr/bin/chromium-browser
ENV CHROME_PATH=/usr/lib/chromium/
