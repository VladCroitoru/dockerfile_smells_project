FROM debian:stretch-slim

RUN groupadd -r overpass && useradd -r -g overpass overpass

ENV OVERPASS_VERSION 0.7.54.10
ENV OVERPASS_DOWNLOAD_URL http://dev.overpass-api.de/releases/osm-3s_v0.7.54.10.tar.gz

RUN buildDeps='wget g++ make libexpat1-dev zlib1g-dev'; \
    apt-get update; \
    apt-get install -y expat uwsgi $buildDeps --no-install-recommends --no-install-suggests; \
    rm -rf /var/lib/apt/lists/*; \
    wget -O overpass.tar.gz $OVERPASS_DOWNLOAD_URL; \
    mkdir -p /usr/src/overpass; \
    tar -xzf overpass.tar.gz -C /usr/src/overpass --strip-components=1; \
    rm overpass.tar.gz; \
    cd /usr/src/overpass; \
    ./configure --prefix=/usr/local; \
    make -j "$(nproc)"; \
    make install; \
    cd /; \
    rm -r /usr/src/overpass; \
    apt-get purge -y --auto-remove $buildDeps

RUN mkdir /data && chown overpass:overpass /data
VOLUME /data
WORKDIR /data

CMD ["uwsgi", "--master", "--http 127.0.0.1:8080"]
