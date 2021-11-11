FROM node:8-alpine
MAINTAINER nownabe <nownabe@gmail.com>

ENV FLOW_VERSION 0.45.0

RUN \
	# To Install Flow Dependencies
	echo "http://dl-cdn.alpinelinux.org/alpine/edge/main" >> /etc/apk/repositories \
  && echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories \
  && echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories \

	# Install Flow Dependencies
  && apk add --update --no-cache --virtual .build-deps \
    bash \
    diffutils \
    elfutils-dev \
    linux-headers \
    m4 \
    ncurses \
    ocaml \
    opam \
    make \
    gcc \
    curl \
    patch \
    make \
    musl-dev \
  && apk add --update --no-cache git elfutils-libelf \
  && apk upgrade libcurl \
  && npm install -g yarn flow-typed \

	# Build & Install Flow
	&& cd /root \
  && opam init -y \
  && eval `opam config env` \
  && opam update \
  && opam install -y ocamlfind sedlex \
  && git clone --depth 1 --branch "v$FLOW_VERSION" https://github.com/facebook/flow.git \
  && cd flow \
  && yarn \
  && make \
  && cp bin/flow /usr/bin/flow \

	# Clean Up
	&& cd .. \
	&& rm -rf /root/flow \
  && apk del .build-deps
