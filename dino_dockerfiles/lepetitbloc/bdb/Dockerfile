FROM debian:stretch-slim

ENV BDB_VERSION="db-4.8.30.NC" \
    BDB_HASH="12edc0df75bf9abd7f82f821795bcee50f42cb2e5f76a6a281b85732798364ef" \
    BDB_DIR="/usr/local/db4"

RUN BDB_FILE=$BDB_VERSION".tar.gz" \
    BDB_URL="http://download.oracle.com/berkeley-db/"$BDB_FILE \
    && set -xe \
    && apt-get update -y \
    && apt-get install -y --no-install-recommends \
        g++ \
        make \
        libdb++-dev \
        autoconf \
        libtool \
        wget \
    && rm -rf /var/lib/apt/lists/* \
    && wget $BDB_URL \
    && echo "$BDB_HASH $BDB_FILE" | sha256sum -c - \
    && tar -xzvf $BDB_FILE \
    && cd $BDB_VERSION"/build_unix/" \
    && ../dist/configure --enable-cxx --disable-shared --with-pic --prefix=$BDB_DIR \
    && mkdir -p $BDB_DIR \
    && make install \
    && cd ../../ \
    && rm $BDB_FILE \
    && rm -rf $BDB_VERSION \
    && export BDB_INCLUDE_PATH="$BDB_DIR/include" \
    && export BDB_LIB_PATH="$BDB_DIR/lib" \
    && ln -s $BDB_DIR/libdb-4.8.so /usr/lib/libdb-4.8.so
