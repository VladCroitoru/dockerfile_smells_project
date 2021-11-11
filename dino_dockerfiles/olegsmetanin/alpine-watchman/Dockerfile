FROM alpine:3.7

RUN apk add --no-cache ca-certificates

RUN apk add --no-cache bash git build-base automake autoconf linux-headers libtool openssl-dev && \
  git clone https://github.com/facebook/watchman.git /tmp/watchman-src && \
  cd /tmp/watchman-src && \
  git checkout v4.9.0 && \
  ./autogen.sh && \
  ./configure --enable-statedir=/tmp --without-python --without-pcre && \
  make && \
  make install && \
  apk del bash git build-base automake autoconf linux-headers libtool openssl-dev && \
  rm -r /tmp/watchman-src
