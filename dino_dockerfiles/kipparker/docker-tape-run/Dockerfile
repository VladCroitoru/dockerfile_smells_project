FROM node:argon
MAINTAINER Kip Parker <kip@kipparker.co.uk>

RUN apt-get update

# Install dependencies for running electron
RUN apt-get install -y \
  xvfb \
  x11-xkb-utils \
  xfonts-100dpi \
  xfonts-75dpi \
  xfonts-scalable \
  xfonts-cyrillic \
  x11-apps \
  clang \
  libdbus-1-dev \
  libgtk2.0-dev \
  libnotify-dev \
  libgnome-keyring-dev \
  libgconf2-dev \
  libasound2-dev \
  libcap-dev \
  libcups2-dev \
  libxtst-dev \
  libxss1 \
  libnss3-dev \
  gcc-multilib \
  g++-multilib

ADD package.json /app/package.json
WORKDIR /app
RUN npm install
# "xvfb-run -a [mycommand]" so xvfb uses another display if 99 is in use.
CMD Xvfb -ac -screen scrn 1280x2000x24 :9.0 & export DISPLAY=:9.0 && npm test
