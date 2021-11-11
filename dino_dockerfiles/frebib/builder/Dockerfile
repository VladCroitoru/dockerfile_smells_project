FROM docker:17.05
MAINTAINER Joe Groocock <frebib@gmail.com>

ARG GLIBC=2.25-r0

RUN apk add --no-cache bash coreutils curl device-mapper gawk git grep iptables openssh sed su-exec tini udev

# Install glibc for docker-compose
RUN curl -o /etc/apk/keys/sgerrand.rsa.pub https://raw.githubusercontent.com/sgerrand/alpine-pkg-glibc/master/sgerrand.rsa.pub && \
    curl -OL https://github.com/sgerrand/alpine-pkg-glibc/releases/download/$GLIBC/glibc-$GLIBC.apk && \
    apk add --no-cache glibc-$GLIBC.apk && rm glibc-$GLIBC.apk && \
    ln -s /lib/libz.so.1 /usr/glibc-compat/lib/ && \
    ln -s /lib/libc.musl-x86_64.so.1 /usr/glibc-compat/lib

# Download and install docker-compose
ARG COMPOSE_VERSION=1.14.0
ADD https://github.com/docker/compose/releases/download/${COMPOSE_VERSION}/docker-compose-linux-x86_64 /usr/local/bin/docker-compose
RUN chmod 755 /usr/local/bin/docker-compose && rm -fr /var/lib/docker/*

# Store github.com SSH fingerprint
RUN mkdir -p ~/.ssh && ssh-keyscan -H github.com | tee -a ~/.ssh/known_hosts

ENV GIT_CLONE_OPTS="--recursive" \
    UID=1000 GID=1000 \
    UNAME=builder \
    GNAME=docker

VOLUME /var/lib/docker

ADD version_list /
ADD bin/* /usr/local/bin/
ENTRYPOINT ["/sbin/tini", "--", "run-docker"]
CMD ["as-builder", "build-image"]
