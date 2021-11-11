FROM alpine:3.12
LABEL maintainer "ant <git@manchestermonkey.co.uk>"

ENV MWH_VERSION 0.12.0

RUN apk add --no-cache python3 py3-cffi py3-pip && \
    apk add --no-cache --virtual .build-deps python3-dev libffi-dev openssl-dev build-base && \
    pip3 install magic-wormhole==${MWH_VERSION} && \
    apk del .build-deps && rm /root/.cache -Rf

WORKDIR /tfr

ENTRYPOINT ["wormhole"]
