FROM debian:stretch-slim

ARG BUILD_DATE

LABEL maintainer="docker@aquaron.com" \
 org.label-schema.build-date=$BUILD_DATE \
 org.label-schema.docker.cmd="docker run --rm -t -v $PWD:/data aquaron/qmk-infinity aquaron.c" \
 org.label-schema.description="Build QMK infinity keyboard" \
 org.label-schema.name="qmk-infinity" \
 org.label-schema.url="https://aquaron.com" \
 org.label-schema.vcs-url="https://github.com/aquaron/qmk-infinity" \
 org.label-schema.vendor="aquaron" \
 org.label-schema.version="1.1"

ENV _examples=/examples \
    _build=/qmk_firmware

RUN apt-get update -qy\
 && apt-get install -qy git make build-essential sudo \
 && git clone https://github.com/qmk/qmk_firmware.git \
 && cd $_build \
 && util/qmk_install.sh \
 && make git-submodule \
# && make infinity60:default \
 && apt-get remove -y git \
 && apt-get -y autoremove \
 && rm -r /var/lib/apt/lists/*

COPY bin/*.c $_examples/
COPY bin/runme.sh /usr/bin

WORKDIR $_build

ENTRYPOINT [ "runme.sh" ]
