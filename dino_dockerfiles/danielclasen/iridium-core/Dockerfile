FROM debian:stretch-slim

ARG IRIDIUM_SRC=https://github.com/iridiumdev/iridium/archive/v4.0.2.tar.gz

RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    libboost-dev \
    libboost-filesystem-dev \
    libboost-system-dev \
    libboost-thread-dev \
    libboost-date-time-dev \
    libboost-chrono-dev \
    libboost-regex-dev \
    libboost-serialization-dev \
    libboost-program-options-dev \
    openssl \
    git \
    wget \
    && mkdir /iridium-src \
    && cd /iridium-src \
    && wget -qO- $IRIDIUM_SRC | tar -xvz --strip 1 \
    && mkdir /iridium-build \
    && cd /iridium-build && CC=/usr/bin/gcc cmake -j`cat /proc/cpuinfo|grep ^processor|wc -l` -D STATIC=ON -D CMAKE_BUILD_TYPE=RELEASE /iridium-src \
    && cd /iridium-build && CC=/usr/bin/gcc PORTABLE=1 make -k -j`cat /proc/cpuinfo|grep ^processor|wc -l` \
    && mkdir /iridium \
    && cp /iridium-build/src/iridium* /iridium/ \
    && rm -rf /iridium-src \
    && rm -rf /iridium-build \
    && apt-get remove -y \
    build-essential \
    cmake \
    libboost-dev \
    libboost-filesystem-dev \
    libboost-system-dev \
    libboost-thread-dev \
    libboost-date-time-dev \
    libboost-chrono-dev \
    libboost-regex-dev \
    libboost-serialization-dev \
    libboost-program-options-dev \
    openssl \
    git \
    wget \
    && apt-get autoremove -y \
    && apt-get clean

RUN mkdir /data \
    && useradd -ms /bin/bash iridium \
    && chown -R iridium /data \
    && chmod 777 -R /data \
    && chmod 777 /iridium

USER iridium
WORKDIR /data

EXPOSE 12007/tcp
EXPOSE 13007/tcp
EXPOSE 14007/tcp

CMD /bin/bash
