# Code maat is written in clojure, but we only need to run the uberjar.
FROM java:8
MAINTAINER Randy Stauner <randy@magnificent-tears.com>

RUN apt-get update \
  && apt-get install -y \
    make \
    git \
    cloc \
    python \
  && rm -rf /var/apt/lists/*

ENV CST_DIR=/usr/src/cst
WORKDIR $CST_DIR

COPY Makefile ./
RUN make

COPY ./bin/ ./bin/

ENV PATH=$CST_DIR/bin:$PATH
