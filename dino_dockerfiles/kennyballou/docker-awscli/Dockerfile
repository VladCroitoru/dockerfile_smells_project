FROM alpine:latest
MAINTAINER kballou@devnulllabs.io

ENV AWSCLI_VERSION="1.16.157"

RUN apk -Uuv add \
    groff \
    less \
    python \
    py-pip && \
    pip install awscli==${AWSCLI_VERSION} && \
    apk --purge -v del \
    py-pip && \
    rm /var/cache/apk/*

WORKDIR "/tmp"

ENTRYPOINT ["aws"]
