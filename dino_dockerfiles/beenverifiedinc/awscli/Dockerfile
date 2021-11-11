FROM alpine:latest
RUN apk upgrade \
    && apk update \
    && apk add python py-pip py-setuptools ca-certificates groff less \
    && pip install awscli \
    && rm -rf /var/cache/apk/*
ENTRYPOINT ["aws"]

