FROM alpine:latest

LABEL maintainer "mikael.brorsson@gmail.com"

RUN apk add --no-cache tini python3 ca-certificates && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    rm -r /root/.cache && \
    apk --update add --no-cache --virtual build-dependencies \
    alpine-sdk python3-dev musl-dev && \
    rm -r /var/cache/apk/* && \
    # pip install pyupio && \
    mkdir -p /opt/ && \
    cd /opt && \
    git clone https://github.com/pyupio/pyup.git && \
    cd pyup && \
    git checkout tags/0.8.2 && \
    pip3 install -e /opt/pyup && \
    apk del build-dependencies

VOLUME /var/spool/cron/crontabs

ENTRYPOINT ["/sbin/tini", "--"]

CMD ["crond", "-f", "-l", "6"]
