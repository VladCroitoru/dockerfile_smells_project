FROM nebo15/alpine-postgre:pglogical
MAINTAINER Nebo#15 <support@nebo15.com>

# Important! Update this no-op ENV variable when this Dockerfile
# is updated with the current date. It will force refresh of all
# of the base images and things like `apt-get update` won't be using
# old cached versions when the Dockerfile is built.
ENV REFRESHED_AT=2017-05-16 \
    LANG=en_US.UTF-8 \
    TERM=xterm \
    HOME=/ \
    CONFD_VERSION=0.12.0-alpha3 \
    PGHOARD_VERSION=f38b187 \
    PGHOARD_BASEBACKUP_COUNT=7 \
    PGHOARD_BASEBACKUP_INTERVAL_HOURS=24 \
    PGHOARD_LOG_LEVEL=INFO \
    PGHOARD_STATSD_PORT=8125 \
    PGHOARD_STATSD_FORMAT=datadog

# Install confd
RUN set -ex; \
    apk add --no-cache --update --virtual .build-deps curl && \
    curl -L -o /usr/local/bin/confd https://github.com/kelseyhightower/confd/releases/download/v${CONFD_VERSION}/confd-${CONFD_VERSION}-linux-amd64 && \
    chmod +x /usr/local/bin/confd && \
    apk del .build-deps

# Install pghoard and it's deps
RUN set -ex; \
    apk add --no-cache --update \
        ca-certificates \
        python3 \
        snappy \
        libffi && \
    apk add --no-cache --update --virtual .build-deps \
        musl-dev \
        python3-dev \
        postgresql-dev \
        snappy-dev \
        libffi-dev \
        gcc \
        g++ && \
    python3 -m ensurepip && \
    pip3 install --upgrade pip setuptools && \
    pip3 install boto azure google google-api-python-client cryptography https://github.com/ohmu/pghoard/archive/master.zip && \
    apk del .build-deps && \
    rm -r /var/cache/apk/*

COPY conf.d /etc/confd/conf.d
COPY templates /etc/confd/templates
COPY docker-entrypoint.sh /bin/docker-entrypoint.sh

ENTRYPOINT ["/bin/bash", "/bin/docker-entrypoint.sh"]
CMD ["/usr/bin/pghoard", "--short-log"]
