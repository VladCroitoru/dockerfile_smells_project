FROM ubuntu:16.04

LABEL vendor="Running Beta" \
  io.runningbeta.maintainer="devops@runningbeta.io" \
  io.runningbeta.version="0.0.1-beta" \
  io.runningbeta.release-date="2017-10-01"

RUN apt-get update && apt-get install -y locales git build-essential cmake libuv1-dev uuid-dev nano

RUN dpkg-reconfigure locales && \
  locale-gen en_US.UTF-8 && \
  update-locale LANG=en_US.UTF-8 LC_CTYPE=en_US.UTF-8 LANGUAGE=en_US:en LC_ALL=en_US.UTF-8

RUN git clone https://github.com/xmrig/xmrig-proxy.git && mv xmrig-proxy xmrig-proxy-dev && \
  cd xmrig-proxy-dev && mkdir build && cd build && \
  cmake .. -DCMAKE_BUILD_TYPE=Release -DUV_LIBRARY=/usr/lib/x86_64-linux-gnu/libuv.a && \
  make && mv xmrig-proxy / && cd ../../ && rm -rf xmrig-proxy-dev

RUN apt-get purge -y git build-essential cmake && rm -rf /var/lib/apt/lists/**

WORKDIR    /
ENTRYPOINT ["./xmrig-proxy"]
