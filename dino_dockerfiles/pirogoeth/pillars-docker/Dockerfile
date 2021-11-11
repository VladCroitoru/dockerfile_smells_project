FROM pirogoeth/py3.5-ci:latest
MAINTAINER Sean Johnson <pirogoeth@maio.me>

RUN apk update
RUN apk add build-base nasm autoconf automake libpng-dev zlib-dev libpng zlib nodejs git python
RUN npm install -g gulp bower
RUN npm install -g imagemin-optipng imagemin-jpegtran imagemin-svgo imagemin-gifsicle
RUN npm install -g phantomjs-prebuilt node-sass ws
