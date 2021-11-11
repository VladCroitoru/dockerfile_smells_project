FROM python:alpine3.14
ARG BUILDPLATFORM
ARG BUILDOS
ARG BUILDARCH
ARG BUILDVARIANT
ARG TARGETPLATFORM
ARG TARGETOS
ARG TARGETARCH
ARG TARGETVARIANT

ENV RTLAMR_VER=v0.9.1

COPY ./rtlamr2mqtt.py /usr/bin
COPY ./requirements.txt /tmp
COPY ./rtlamt2mqtt.yaml /etc

WORKDIR /tmp
RUN echo "Building to: ${TARGETARCH}" \
    && apk update \
    && apk add rtl-sdr \
    && pip3 install -r /tmp/requirements.txt \
    && chmod 755 /usr/bin/rtlamr2mqtt.py \
    && wget https://github.com/bemasher/rtlamr/releases/download/${RTLAMR_VER}/rtlamr_linux_${TARGETARCH}.tar.gz \
    && tar zxvf rtlamr_linux_${TARGETARCH}.tar.gz \
    && chmod 755 rtlamr \
    && mv rtlamr /usr/bin \
    && rm -f /tmp/*
    
RUN \
    set -o pipefail \
    \
    && apk update \
    && apk add --no-cache --virtual .build-dependencies \
        tar=1.34-r0 \
    \
    && apk add --no-cache \
        libcrypto1.1=1.1.1l-r0 \
        libssl1.1=1.1.1l-r0 \
        musl-utils=1.2.2-r3 \
        musl=1.2.2-r3 \
    \
    && apk add --no-cache \
        bash=5.1.4-r0 \
        curl=7.79.1-r0 \
        jq=1.6-r1 \
        tzdata=2021a-r0 \
    \
    && case ${TARGETPLATFORM} in \
         "linux/amd64")  BUILD_ARCH=amd64  ;; \
         "linux/arm64")  BUILD_ARCH=aarch64  ;; \
         "linux/arm/v7") BUILD_ARCH=armv7  ;; \
         "linux/arm/v6") BUILD_ARCH=armhf   ;; \
         "linux/386")    BUILD_ARCH=i386   ;; \
    esac \
    && S6_ARCH="${BUILD_ARCH}" \
    && if [ "${BUILD_ARCH}" = "i386" ]; then S6_ARCH="x86"; fi \
    && if [ "${BUILD_ARCH}" = "armv7" ]; then S6_ARCH="arm"; fi \
    \
    && curl -L -s "https://github.com/just-containers/s6-overlay/releases/download/v2.2.0.3/s6-overlay-${S6_ARCH}.tar.gz" \
        | tar zxvf - -C / \
    \
    && mkdir -p /etc/fix-attrs.d \
    && mkdir -p /etc/services.d \
    \
    && curl -J -L -o /tmp/bashio.tar.gz \
        "https://github.com/hassio-addons/bashio/archive/v0.13.1.tar.gz" \
    && mkdir /tmp/bashio \
    && tar zxvf \
        /tmp/bashio.tar.gz \
        --strip 1 -C /tmp/bashio \
    \
    && mv /tmp/bashio/lib /usr/lib/bashio \
    && ln -s /usr/lib/bashio/bashio /usr/bin/bashio \
    \
    && curl -L -s -o /usr/bin/tempio \
        "https://github.com/home-assistant/tempio/releases/download/2021.05.0/tempio_${BUILD_ARCH}" \
    && chmod a+x /usr/bin/tempio \
    \
    && apk del --no-cache --purge .build-dependencies \
    && rm -f -r \
        /tmp/*
        
STOPSIGNAL SIGTERM
CMD ["/usr/bin/rtlamr2mqtt.py","/etc/rtlamt2mqtt.yaml"] 