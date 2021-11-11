FROM node:12-alpine

ADD . /srv
WORKDIR /srv

# sharp needs python installed in Alpine
RUN apk add --update \
    python \
    python-dev \
    py-pip \
    build-base \
    autoconf \
    automake \
    make \
    gcc \
    g++ \
    libtool \
    pkgconfig \
    nasm \
  && pip install virtualenv \
  && rm -rf /var/cache/apk/*

RUN npm install
RUN npm run build

CMD npm run serve
