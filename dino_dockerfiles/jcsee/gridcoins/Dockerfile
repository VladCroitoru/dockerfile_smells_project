FROM ubuntu:16.04
ENV DEBIAN_FRONTEND=noninteractive \
    USERNAME=g \
    HOME=/home/g \
    VERSION=3.7.11.0

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
      ca-certificates \
      git gcc make curl build-essential libssl-dev libdb-dev libdb++-dev libqrencode-dev libcurl4-openssl-dev libzip-dev libzip4 libboost-all-dev \
      less \
      net-tools \
 && rm -rf /var/lib/apt/lists/*

RUN cd /usr/src/ \
 && git clone -b $VERSION https://github.com/gridcoin/Gridcoin-Research \
 && apt-get purge -y git \
 && cd Gridcoin-Research/src \
 && grep CLIENT_VERSION clientversion.h \
 && mkdir -p obj/zerocoin && chmod +x leveldb/build_detect_platform \
 && make -f makefile.unix clean \
 && make -f makefile.unix USE_UPNP=- \
 && strip gridcoinresearchd \
 && install -m 755 gridcoinresearchd /usr/bin/gridcoinresearchd \
 && rm -rf /usr/src/Gridcoin-Research \
 && mkdir /var/lib/boinc-client

RUN useradd --uid 1000 --groups dialout --no-create-home --shell /bin/bash --home-dir $HOME $USERNAME \
        && mkdir $HOME \
        && chown -R $USERNAME:$USERNAME $HOME

VOLUME $HOME/.GridcoinResearch/ /var/lib/boinc-client/

USER $USERNAME

WORKDIR $HOME
