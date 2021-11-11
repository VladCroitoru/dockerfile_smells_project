FROM mhart/alpine-node:8
MAINTAINER denso.ffff@gmail.com

# Pinger
RUN apk add --no-cache \
        curl \
        git \
        build-base \
        g++ \
        cairo-dev \
        jpeg-dev \
        pango-dev \
        giflib-dev

RUN apk update && apk add --no-cache fontconfig curl && \
  mkdir -p /usr/share && \
  cd /usr/share \
  && curl -L https://github.com/Overbryd/docker-phantomjs-alpine/releases/download/2.11/phantomjs-alpine-x86_64.tar.bz2 | tar xj \
  && ln -s /usr/share/phantomjs/phantomjs /usr/bin/phantomjs \
  && phantomjs --version

COPY package.json /srv/package.json
RUN cd /srv/ && npm install # packages are installed globally to not modify Pinger directory

RUN npm install -g gulp

WORKDIR /srv/www
COPY . /srv/www/
RUN gulp

EXPOSE 5001
CMD cd /srv/www/ && rm -fr node_modules && \
    gulp watch
