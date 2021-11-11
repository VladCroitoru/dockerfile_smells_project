ARG BUILD_FROM
FROM $BUILD_FROM as build

# Install build packages
RUN apk update && \
    apk add --no-cache build-base git cmake sqlite-dev curl-dev linux-headers autoconf automake libtool zlib-dev


## vbus-collector
FROM build as build-collector
ARG COLLECTOR_VERSION=master

RUN mkdir /src && cd /src && \
    git clone https://github.com/tripplet/vbus-collector.git --recursive --single-branch --branch $COLLECTOR_VERSION --depth 1 /src/collector

RUN cd /src/collector/paho.mqtt.c && \
    mkdir build && cd build && \
    cmake -DPAHO_BUILD_STATIC=TRUE -DPAHO_ENABLE_CPACK=FALSE -DPAHO_HIGH_PERFORMANCE=TRUE .. && \
    make -j

RUN cd /src/collector/cJSON && \
    mkdir build && cd build && \
    cmake -DBUILD_SHARED_LIBS=OFF -DENABLE_CJSON_TEST=OFF -DENABLE_CJSON_UTILS=OFF -DENABLE_LOCALES=OFF .. && \
    make -j

RUN cd /src/collector && make -j && strip vbus-collector


## vbus-server
FROM build as build-server
ARG SERVER_VERSION=master

RUN mkdir /src && cd /src && \
    git clone https://github.com/tripplet/vbus-server.git --recursive --single-branch --branch $SERVER_VERSION --depth 1 /src/server

ARG BROTLI_SUPPORT=0
RUN cd /src/server && \
    cmake -DCMAKE_BUILD_TYPE=Release -DBROTLI_SUPPORT=$BROTLI_SUPPORT -DDB_PATH=/data/data.db . && \
    make -j && strip vbus-server

## Final image
FROM alpine

RUN apk update --no-cache && \
    apk add --no-cache tzdata libstdc++ libcurl zlib sqlite-libs nginx fcgiwrap jq picocom

COPY --from=build-collector /src/collector/vbus-collector /bin/vbus-collector
COPY --from=build-server /src/server/web/* /htdocs/

COPY rootfs /

RUN chown -R nginx: /htdocs && \
    chmod o+w /run

## General stuff

LABEL maintainer="Tobias Tangemann"
LABEL io.hass.version="1.0" io.hass.type="addon" io.hass.arch="armhf|aarch64|amd64"

ENTRYPOINT ["/init"]
HEALTHCHECK --interval=5m --timeout=10s --start-period=10s CMD /healthcheck.sh 5
