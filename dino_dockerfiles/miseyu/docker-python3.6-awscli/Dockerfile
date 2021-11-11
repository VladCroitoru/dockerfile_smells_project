FROM alpine:3.6

ENV LANG C.UTF-8

RUN apk --no-cache update && \
    apk add --no-cache gcc make libc-dev libxslt-dev libxml2-dev findutils musl-dev build-base && \
    apk add --no-cache python3 python3-dev && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    apk --no-cache add ca-certificates curl groff less tzdata && \
    cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime && \
    apk del tzdata && \
    apk --no-cache add bash jq && \
    apk add --no-cache --virtual .build-deps g++ && \
    ln -s /usr/include/locale.h /usr/include/xlocale.h && \
    pip --no-cache-dir install --upgrade pip && \
    pip --no-cache-dir install awscli && \
    rm -rf /var/cache/apk/*
