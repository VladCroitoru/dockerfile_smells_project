FROM ubuntu:xenial
ARG VERSION=2.0.2

RUN apt-get update && apt-get -y install \
  git \
  build-essential \
  cmake \
  libpcap-dev \
  python \
  zlib1g-dev \
  libssl-dev

# Get dependencies, link, compile, and install (combined to avoid HUGE, 10G+ intermediate images)
RUN mkdir -p /var/downloads \
  && cd /var/downloads \
  && git clone https://github.com/Tokutek/mongo \
  && git clone https://github.com/Tokutek/ft-index \
  && git clone https://github.com/Tokutek/jemalloc \
  && git clone https://github.com/Tokutek/backup-community \
  && cd /var/downloads/mongo \
  && git checkout tokumx-$VERSION \
  && cd /var/downloads/ft-index \
  && git checkout tokumx-$VERSION \
  && cd /var/downloads/jemalloc \
  && git checkout tokumx-$VERSION \
  && cd /var/downloads/backup-community \
  && git checkout tokumx-$VERSION \
  && cd /var/downloads/mongo \
  && ln -snf `pwd`/../jemalloc ../ft-index/third_party/jemalloc \
  && ln -snf `pwd`/../ft-index src/third_party/ft-index \
  && ln -snf `pwd`/../backup-community/backup src/third_party/backup \
  && mkdir build \
  && cd build \
  && cmake -D BUILD_TESTING=OFF -D USE_VALGRIND=OFF -D CMAKE_BUILD_TYPE=Debug -D TOKU_DEBUG_PARANOID=ON -D USE_CSCOPE=OFF -D USE_CTAGS=OFF -D USE_ETAGS=OFF -D USE_GTAGS=OFF -D USE_SSL=ON -D TOKUMX_DISTNAME=${VERSION}-ssl .. \
  && make -j4 package \
  && tar xzf tokumx-${VERSION}-ssl-linux-x86_64-debug-main.tar.gz -C /opt \
  && ln -sf /opt/tokumx-${VERSION}-ssl-linux-x86_64-debug/bin/* /usr/local/bin \
  && mkdir -p /data/db \
  && rm -rf /var/downloads/*

EXPOSE 27017
ENTRYPOINT ["/usr/local/bin/mongod"]
