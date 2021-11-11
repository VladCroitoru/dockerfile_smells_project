FROM alpine:edge

# Set env to detect if we are in a container, or not
ENV CONTAINER=1

USER root

# Install base
RUN apk update
RUN apk upgrade
RUN apk add \
  wget \
  bash \
  chromium \
  chromium-chromedriver \
  curl \
  git \
  wget \
  autoconf \
  nodejs \
  nodejs-npm \
  automake \
  sudo \
  g++ \
  make \
  perl \
  libffi-dev \
  bash \
  python2 \
  file \
  nasm \
  libsass \
  xvfb \
  libx11 \
  randrproto \
  xineramaproto \
  imagemagick \
  libjpeg-turbo-utils \
  gifsicle \
  optipng \
  udev \
  libc6-compat \
  zlib-dev \
  wait4ports \
  xorg-server \
  dbus \
  ttf-freefont \
  mesa-dri-swrast \
  openjdk8

ENV JAVA_HOME $(dirname "$(readlink -f "$(which javac || which java)")")

# Prepare Workdir
RUN addgroup node
RUN adduser -S node
RUN mkdir /var/www
RUN chown node:node /var/www
RUN echo "node ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
RUN chmod 777 -R /var/log/

# Install npm dependencies
RUN npm install -g bower gulp-cli protractor

USER node

WORKDIR /var/www