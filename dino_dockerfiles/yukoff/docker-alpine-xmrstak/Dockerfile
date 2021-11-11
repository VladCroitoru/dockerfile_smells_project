FROM alpine:latest
COPY donate-level.patch /tmp/
COPY start.sh /xmr-stak/
COPY config.txt.tpl /xmr-stak/
RUN adduser -S -D -H -h /xmr-stak miner
RUN apk --no-cache upgrade && \
    apk --no-cache add \
      git \
      cmake \
      g++ \
      openssl \
      openssl-dev \
      build-base && \
    git clone https://github.com/fireice-uk/xmr-stak.git /tmp/xmr-stak && \
    cd /tmp/xmr-stak && \
      patch -p1 < /tmp/donate-level.patch && \
      mkdir build && \
      cd build && \
      cmake -DCMAKE_BUILD_TYPE=Release \
            -DCMAKE_INSTALL_PREFIX=/xmr-stak \
            -DCMAKE_LINK_STATIC=ON \
            -DMICROHTTPD_ENABLE=OFF \
            -DCUDA_ENABLE=OFF \
            -DOpenCL_ENABLE=OFF \
            -DHWLOC_ENABLE=OFF \
            .. && \
      make install && \
    cd /xmr-stak && \
    rm -rf /tmp/*.patch /tmp/xmr-stak && \
    apk del \
      build-base \
      openssl-dev \
      g++ \
      cmake \
      git
USER miner
WORKDIR /xmr-stak
ENTRYPOINT ["/xmr-stak/start.sh"]
#CMD ["pool_url", "wallet", "password", "workers"]
