FROM alpine:3.7
LABEL maintainer="Henry McConville <henry.mcconville@infinityworks.com>"

RUN apk --update add --no-cache  \
    python && \
    apk --update add --no-cache --virtual build-dependencies \
    py-pip \
    python-dev \
    build-base && \
    mkdir -p /var/awslogs/state && \
    mkdir -p /var/awslogs/etc/config && \
    pip install --upgrade \
    --extra-index-url=http://aws-cloudwatch.s3-website-us-east-1.amazonaws.com/ \
    --trusted-host=aws-cloudwatch.s3-website-us-east-1.amazonaws.com \
    awscli-cwlogs && \
    apk del build-dependencies && \
    rm -rf /var/cache/apk/* /root/.cache/* /usr/share/terminfo

ADD boot.sh /var/awslogs

ENTRYPOINT ["/bin/sh", "/var/awslogs/boot.sh"]