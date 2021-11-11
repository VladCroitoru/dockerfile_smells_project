FROM phusion/baseimage

ARG QBITTORRENT_VERSION=3.3.12

ENV USER_ID 107
ENV GROUP_ID 114
ENV BUILD_PACKAGES git python libboost-dev libboost-system-dev build-essential libqt4-dev qtbase5-dev qttools5-dev-tools libboost-system-dev libboost-chrono-dev libboost-random-dev libssl-dev libgeoip-dev pkg-config automake libtool

RUN apt-get update && \
  # General required dependencies
  apt-get install -y geoip-database $BUILD_PACKAGES && \
  
  # Build Libtorrent
  git clone https://github.com/arvidn/libtorrent.git /usr/src/libtorrent && \
  cd /usr/src/libtorrent && \
  git checkout RC_1_1 && \
  ./autotool.sh && \
  ./configure --disable-debug --enable-encryption --prefix=/usr --with-libgeoip=system CXXFLAGS=-std=c++11 && \
  make clean && make && \
  make install && \
  
  # Download qBittorrent
  git clone https://github.com/qbittorrent/qBittorrent.git /usr/src/qbittorrent && \
  cd /usr/src/qbittorrent && \
  git checkout release-${QBITTORRENT_VERSION} && \
  ./configure --prefix=/usr --disable-gui --enable-debug && \
  make && \
  make install && \
  cd && \

  # Clean up
  apt-get purge -y $BUILD_PACKAGES && \
  rm -rf /usr/src/qbittorrent && \
  rm -rf /usr/src/libtorrent && \
  rm -rf /var/lib/apt/lists/*

COPY ./entrypoint.sh /

VOLUME ["/config", "/torrents", "/downloads"]



ENTRYPOINT ["/entrypoint.sh"]

CMD ["qbittorrent-nox"]
