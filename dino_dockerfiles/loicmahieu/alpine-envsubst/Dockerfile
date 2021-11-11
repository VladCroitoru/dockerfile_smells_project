FROM alpine:3.4

ENV \
    BUILD_DEPS="gettext"  \
    RUNTIME_DEPS="libintl"

RUN \
    apk add --update $RUNTIME_DEPS && \
    apk add --virtual build_deps $BUILD_DEPS &&  \
    cp /usr/bin/envsubst /usr/local/bin/envsubst && \
    apk del build_deps

ENTRYPOINT /usr/local/bin/envsubst
