FROM alpine:3.6

RUN apk add --update --no-cache \
    python \
    python-dev \
    py-pip \
    build-base \
    ca-certificates \
    libffi-dev \
    openssl-dev \
    && pip install roca-detect \
    && rm -rf /var/cache/apk/*

CMD ["roca-detect", "/keys"]
