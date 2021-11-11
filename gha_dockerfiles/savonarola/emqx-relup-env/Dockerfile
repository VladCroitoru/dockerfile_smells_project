FROM emqx/build-env:erl23.2.7.2-emqx-2-ubuntu20.04

ARG CREATED
ARG VERSION
ARG REF

LABEL org.opencontainers.image.created=$CREATED
LABEL org.opencontainers.image.authors="Ilya Averyanov <ilya.averyanov@emqx.io>"
LABEL org.opencontainers.image.url="https://github.com/savonarola/emqx-relup-env"
LABEL org.opencontainers.image.documentation="https://github.com/savonarola/emqx-relup-env/README.md"
LABEL org.opencontainers.image.source="https://github.com/savonarola/emqx-relup-env"
LABEL org.opencontainers.image.version=$VERSION
LABEL org.opencontainers.image.revision=$REF
LABEL org.opencontainers.image.vendor="Ilya Averyanov"
LABEL org.opencontainers.image.licenses="Apache License"
LABEL org.opencontainers.image.title="EMQX Relup Test Prebuilt Env"
LABEL org.opencontainers.image.description="Image Containing Tools For Running EMQX Release Upgrade Tests"


RUN mkdir /tools

ARG MQTT_BENCH_REF
ENV MQTT_BENCH_REF=${MQTT_BENCH_REF:-0.3.3}

RUN git clone --depth=1 --branch=${MQTT_BENCH_REF} https://github.com/emqx/emqtt-bench.git /tools/emqtt-bench
RUN make -C /tools/emqtt-bench

ENV PATH="/tools/emqtt-bench:$PATH"

ARG LUX_REF
ENV LUX_REF=${LUX_REF:-lux-2.6}

RUN git clone --depth=1 --branch=${LUX_REF} https://github.com/hawk/lux /tools/lux
WORKDIR /tools/lux

RUN autoconf && \
    ./configure && \
    make && \
    make install
