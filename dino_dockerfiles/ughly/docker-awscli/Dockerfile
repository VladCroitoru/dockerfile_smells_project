FROM docker:latest

RUN apk --no-cache update && \
    apk --no-cache add python py-pip py-setuptools ca-certificates groff less && \
    pip --no-cache-dir install awscli && \
    apk -v --purge del py-pip && \
    rm -rf /var/cache/apk/*
