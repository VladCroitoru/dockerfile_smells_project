FROM alpine:3.3
MAINTAINER Stefano Da Ros "sd@cip.li"

WORKDIR /app
ENV HOME /app
ENV ARCH "rem-Linux-x86_64"
ENV RELEASE "https://github.com/sdaros/rem/releases/download/v0.6.0"

RUN apk add --no-cache ca-certificates && \
    apk add --no-cache tzdata && \
    apk add --no-cache curl && \
    curl -LO ${RELEASE}/${ARCH} && \
    chmod +x ${ARCH} && \
    mkdir -p .config/rem && \
    mv ${ARCH} /usr/local/bin/rem
EXPOSE 42888
COPY rem.conf .config/rem/rem.conf
ENTRYPOINT rem
