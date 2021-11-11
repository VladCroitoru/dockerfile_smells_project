FROM docker:stable-git

RUN apk update && \
    apk add py-pip bash jq && \
    pip install docker-compose && \
    apk add rsync && \
    apk add -U --no-cache --repository http://dl-3.alpinelinux.org/alpine/edge/testing gnu-libiconv

ENV LD_PRELOAD "/usr/lib/preloadable_libiconv.so"
