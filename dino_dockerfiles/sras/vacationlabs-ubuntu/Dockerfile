FROM ubuntu:14.04

RUN apt-get update \
  && apt-get install -y --force-yes curl \
  && apt-get install -y --force-yes --no-install-recommends \
  make \
  xz-utils \
  libpq-dev \
  libicu-dev \
  libblas-dev \
  liblapack-dev \
  libgmp3-dev \
  clang \
  gcc \
  && cd /tmp \
  && curl -L https://github.com/commercialhaskell/ghc/releases/download/ghc-8.0.2-release/ghc-8.0.2-x86_64-deb7-linux.tar.xz > ghc-8.0.2.tar.xz \
  && tar -xf "ghc-8.0.2.tar.xz" \
  && cd ghc-8.0.2 \
  && ./configure && /usr/bin/make install \
  && rm -rf ghc-8.0.2.tar.xz ghc-8.0.2 \
  && curl -sSL https://get.haskellstack.org/ | sh \
  && apt-get remove -y --force-yes curl \
  && apt-get remove -y --force-yes xz-utils \
  && rm -rf /var/lib/apt/lists/*
