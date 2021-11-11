FROM alpine:3.5

MAINTAINER Nebo#15 support@nebo15.com

# Install gosu
ENV GOSU_VERSION=1.10
RUN set -x && \
    apk add --no-cache --virtual .gosu-deps \
        dpkg \
        gnupg \
        openssl && \
    dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')" && \
    wget -O /usr/local/bin/gosu "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch" && \
    wget -O /usr/local/bin/gosu.asc "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc" && \
    export GNUPGHOME="$(mktemp -d)" && \
    gpg --keyserver ha.pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4 && \
    gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu && \
    rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc && \
    chmod +x /usr/local/bin/gosu && \
    gosu nobody true && \
    apk --purge del .gosu-deps

# Configure environment variables and other settings
ENV REFRESHED_AT=2017-02-21 \
    HOME=/data \
    DB_PATH=/data/db \
    MONGODB_VERSION=3.2.10-r1

# You should override it in your Docker environment to match how much memory you want to allocate for mongodb
ENV MAX_RAM=1GB

# Performance tuning
RUN echo "net.core.somaxconn = 3072" >> /etc/sysctl.conf && \
    echo "net.ipv4.tcp_max_syn_backlog = 4096" >> /etc/sysctl.conf && \
    echo "net.ipv4.conf.default.rp_filter = 0" >> /etc/sysctl.conf && \
    echo "net.ipv4.tcp_keepalive_time = 120" >> /etc/sysctl.conf && \
    echo "fs.file-max = 2097152" >> /etc/sysctl.conf

# Install MongoDB
RUN echo "@edge http://nl.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories && \
    apk --no-cache --update add mongodb@edge=$MONGODB_VERSION && \
    # rm /usr/bin/mongosniff /usr/bin/mongoperf && \
    rm -rf /var/cache/apk/*

# Add entrypoint
COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
ENTRYPOINT ["docker-entrypoint.sh"]

# Expose data volume
RUN mkdir -p $HOME && \
    mkdir -p $DB_PATH && \
    chmod -R 777 $HOME $DB_PATH && \
    cd $HOME
WORKDIR $HOME
VOLUME $DB_PATH

# Expose MongoDB ports
EXPOSE 27017 28017

CMD ["mongod"]
