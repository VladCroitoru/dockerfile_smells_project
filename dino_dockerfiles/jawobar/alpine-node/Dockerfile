FROM mhart/alpine-node:6.3.0

ENV \
  GULP_VERSION=3.9.1 \
  TYPINGS_VERSION=1.3.1
  
RUN apk add --update curl bash && \
  curl -Ls "https://github.com/dustinblackman/phantomized/releases/download/2.1.1/dockerized-phantomjs.tar.gz" | tar xz -C / && \
  apk del curl

RUN npm install -g \
  gulp@${GULP_VERSION} \
  typings@${TYPINGS_VERSION}

RUN find /usr/lib/node_modules -name test -o -name .bin -type d | xargs rm -rf
