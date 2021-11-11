FROM  alpine:latest

LABEL vendor="Running Beta" \
  io.runningbeta.maintainer="devops@runningbeta.io" \
  io.runningbeta.version="0.0.1-beta" \
  io.runningbeta.release-date="2017-10-01"

RUN   adduser -S -D -H -h /xmrig miner
RUN   apk --no-cache upgrade && \
      apk --no-cache add \
        git \
        cmake \
        libuv-dev \
        build-base && \
      git clone https://github.com/xmrig/xmrig && \
      cd xmrig && \
      mkdir build && \
      cmake -DCMAKE_BUILD_TYPE=Release . && \
      make && \
      apk del \
        build-base \
        cmake \
        git
USER miner
WORKDIR    /xmrig
ENTRYPOINT  ["./xmrig", "--donate-level=5"]
