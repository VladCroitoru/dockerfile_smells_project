FROM alpine:3.9

ENV CLASSPATH="./build/classes/main:./build/resources/main:./build/elasticio/dependencies/*"
ENV ALPINE_GLIBC_BASE_URL="https://github.com/sgerrand/alpine-pkg-glibc/releases/download"
ENV ALPINE_GLIBC_PACKAGE_VERSION="2.27-r0"
ENV ALPINE_GLIBC_BASE_PACKAGE_FILENAME="glibc-$ALPINE_GLIBC_PACKAGE_VERSION.apk"
ENV ALPINE_GLIBC_BIN_PACKAGE_FILENAME="glibc-bin-$ALPINE_GLIBC_PACKAGE_VERSION.apk"

RUN addgroup -S apprunner && \
    adduser -S apprunner -G apprunner -h /home/apprunner

USER root
RUN apk add --no-cache curl && \
    apk add --no-cache libstdc++ && \
    apk add --no-cache openjdk8-jre-base && \
    apk add --no-cache nss && \
    apk add --no-cache --repository http://dl-3.alpinelinux.org/alpine/edge/community tini && \
    curl -s -L -o "$ALPINE_GLIBC_BASE_PACKAGE_FILENAME" "$ALPINE_GLIBC_BASE_URL/$ALPINE_GLIBC_PACKAGE_VERSION/$ALPINE_GLIBC_BASE_PACKAGE_FILENAME" && \
    curl -s -L -o "$ALPINE_GLIBC_BIN_PACKAGE_FILENAME" "$ALPINE_GLIBC_BASE_URL/$ALPINE_GLIBC_PACKAGE_VERSION/$ALPINE_GLIBC_BIN_PACKAGE_FILENAME" && \
    apk add --no-cache --allow-untrusted "$ALPINE_GLIBC_BASE_PACKAGE_FILENAME" && \
    apk add --no-cache --allow-untrusted "$ALPINE_GLIBC_BIN_PACKAGE_FILENAME" && \
    rm "$ALPINE_GLIBC_BASE_PACKAGE_FILENAME" "$ALPINE_GLIBC_BIN_PACKAGE_FILENAME"

USER apprunner
COPY --chown=apprunner:apprunner bin/run.sh /run.sh

ENTRYPOINT ["/sbin/tini", "-v", "-e", "143", "--", "/run.sh"]
