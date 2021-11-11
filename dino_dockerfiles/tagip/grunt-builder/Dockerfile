FROM node:4-alpine

RUN apk add --update --no-cache \
  openssh-client \
  automake \
  git \
  alpine-sdk  \
  nasm  \
  autoconf  \
  build-base \
  zlib \
  zlib-dev \
  libpng \
  libpng-dev\
  libwebp \
  libwebp-dev \
  libjpeg-turbo \
  libjpeg-turbo-dev \
  libjpeg-turbo-utils

RUN apk add --no-cache --repository http://dl-3.alpinelinux.org/alpine/edge/community/ --allow-untrusted \
  gifsicle \
  optipng \
  pngquant


RUN npm i -g grunt-cli bower svgo && \
  grunt -V && \
  bower -v
