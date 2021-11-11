FROM alpine:latest

ENV APP_PKGS="ca-certificates"
ENV BUILD_PKGS="wget"

ENV OAUTH2_PROXY_VERSION="2.2"
ENV OAUTH2_PROXY_PKG="oauth2_proxy-2.2.0.linux-amd64.go1.8.1" \
    OAUTH2_PROXY_SHA="1c16698ed0c85aa47aeb80e608f723835d9d1a8b98bd9ae36a514826b3acce56"
RUN apk update && \
    apk upgrade && \
    apk add $APP_PKGS $BUILD_PKGS && \
    mkdir -p /var/tmp/oauth2_proxy && \
    cd /var/tmp/oauth2_proxy && \
    wget --progress=dot:mega https://github.com/bitly/oauth2_proxy/releases/download/v${OAUTH2_PROXY_VERSION}/${OAUTH2_PROXY_PKG}.tar.gz && \
    echo "${OAUTH2_PROXY_SHA} *${OAUTH2_PROXY_PKG}.tar.gz" | sha256sum -c - && \
    tar xvf ${OAUTH2_PROXY_PKG}.tar.gz && \
    cp /var/tmp/oauth2_proxy/${OAUTH2_PROXY_PKG}/oauth2_proxy /bin/ && \
    apk del $BUILD_PKGS && \
    rm -rf /var/cache/apk/*

EXPOSE 4180

ENTRYPOINT ["oauth2_proxy"]
