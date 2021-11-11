ARG BDB_VERSION="4.8.30.NC"

FROM lepetitbloc/bdb:$BDB_VERSION

LABEL maintainer="johan@lepetitbloc.net"

ARG USE_UPNP=1
ARG WALLET="sparks"
ARG BASE_DIR=".sparkscore/"
ARG CONFIG_FILE="sparks.conf"
ARG PORT=8890
ARG RPC_PORT=8892
ARG REPOSITORY="https://github.com/SparksReborn/sparkspay.git"
ARG REF="tags/v0.12.3.2"

ENV USE_UPNP=$USE_UPNP \
    WALLET=$WALLET \
    BASE_DIR=$BASE_DIR \
    CONFIG_FILE=$CONFIG_FILE \
    PORT=$PORT \
    RPC_PORT=$RPC_PORT

EXPOSE $PORT $RPC_PORT

RUN apt-get update -y && apt-get install -y \
    libssl-dev \
    libboost-system-dev \
    libboost-filesystem-dev \
    libboost-chrono-dev \
    libboost-program-options-dev \
    libboost-test-dev \
    libboost-thread-dev \
    libminiupnpc-dev \
    libgmp-dev \
    libevent-dev \
    libzmq3-dev \
    automake \
    pkg-config \
    git \
    bsdmainutils \
&& rm -rf /var/lib/apt/lists/* \
&& useradd -lrUm $WALLET \
&& git clone $REPOSITORY /tmp/$WALLET

WORKDIR /tmp/$WALLET

# build
RUN git fetch --tags \
&&  git checkout $REF \
&&  chmod +x autogen.sh share/genbuild.sh src/leveldb/build_detect_platform \
&&  sync \
&&  ./autogen.sh \
&&  ./configure CPPFLAGS="-I/usr/local/db4/include -O2" LDFLAGS="-L/usr/local/db4/lib" \
&&  make \
&&  strip src/${WALLET}d src/${WALLET}-cli src/${WALLET}-tx \
&&  mv src/${WALLET}d /usr/local/bin/ \
&&  mv src/${WALLET}-cli /usr/local/bin/ \
&&  mv src/${WALLET}-tx /usr/local/bin/ \
&&  rm -rf /tmp/$WALLET

USER $WALLET

WORKDIR /home/$WALLET

RUN mkdir -p data $BASE_DIR

COPY wallet/${BASE_DIR}masternode.conf ${BASE_DIR}masternode.conf
COPY wallet/$BASE_DIR$CONFIG_FILE $BASE_DIR$CONFIG_FILE
COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh

ENTRYPOINT ["docker-entrypoint.sh"]
