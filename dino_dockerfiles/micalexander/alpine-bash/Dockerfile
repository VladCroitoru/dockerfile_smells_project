FROM alpine:edge

MAINTAINER Michael Alexander <michael@micalexander.com>

RUN apk add --update --update-cache \
  alpine-sdk \
  autoconf \
  automake \
  argon2-libs \
  bash \
  bash-completion \
  bzip2 \
  ctags \
  curl \
  docker \
  file \
  findutils \
  freetype-dev \
  gdbm \
  grep \
  htop \
  jq \
  libedit-dev \
  libffi-dev \
  libmcrypt \
  libnotify \
  libpng-dev \
  libressl2.7-libcrypto \
  libressl2.7-libssl \
  libsodium \
  libxml2-dev \
  libxslt-dev \
  linux-headers \
  man \
  mysql-client \
  mosh \
  nasm \
  ncurses \
  neovim \
  neovim-doc \
  openrc \
  openssh \
  openssl-dev \
  pcre-dev \
  perl \
  procps \
  rsync \
  sed \
  shadow \
  sqlite-libs \
  sshpass \
  tcpdump \
  the_silver_searcher \
  tmux \
  tree \
  tzdata \
  unzip \
  wget \
  yaml-dev \
  yarn \
  && rm -rf /var/cache/apk/*
  
RUN apk add libssl1.0 --repository=http://nl.alpinelinux.org/alpine/v3.8/main \
  && rm -rf /var/cache/apk/*

COPY dev_user.yml /usr/local/bin/
COPY docker-bash-entrypoint /usr/local/bin/

ENTRYPOINT ["docker-bash-entrypoint"]
