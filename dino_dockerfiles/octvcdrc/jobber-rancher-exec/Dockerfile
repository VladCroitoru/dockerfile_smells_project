#We need alpine 3.4 due to an issue when building go things. https://bugs.alpinelinux.org/issues/6628
FROM alpine:3.4

#Based on https://github.com/blacklabelops/jobber-cron and https://github.com/meltwater/docker-cleanup
MAINTAINER Cedric Octave <docker@octvcdrc.fr>

RUN apk upgrade --update && apk add \
      bash \
      tini \
      docker \
      jq \
      sed \
      grep

ARG JOBBER_VERSION=latest

RUN export JOBBER_HOME=/tmp/jobber && \
    export JOBBER_LIB=$JOBBER_HOME/lib && \
    export GOPATH=$JOBBER_LIB && \
    export CONTAINER_UID=1000 && \
    export CONTAINER_GID=1000 && \
    export CONTAINER_USER=jobber_client && \
    export CONTAINER_GROUP=jobber_client && \
    apk add --update \
      go \
      git \
      curl \
      wget \
      make && \
    mkdir -p $JOBBER_HOME && \
    mkdir -p $JOBBER_LIB && \
    # Install Jobber
    addgroup -g $CONTAINER_GID jobber_client && \
    adduser -u $CONTAINER_UID -G jobber_client -s /bin/bash -S jobber_client && \
    cd $JOBBER_LIB && \
    go get github.com/dshearer/jobber;true && \
    make -C src/github.com/dshearer/jobber install DESTDIR=$JOBBER_HOME && \
    cp $JOBBER_LIB/bin/* /usr/bin && \
    apk del \
      go \
      git \
      curl \
      wget \
      make && \
    rm -rf /var/cache/apk/* && rm -rf /tmp/* && rm -rf /var/log/*

COPY docker-entrypoint.sh /opt/jobber/docker-entrypoint.sh
COPY rancher-exec.sh /usr/bin/rancher-exec
RUN chmod u+x /opt/jobber/docker-entrypoint.sh
RUN chmod u+x /usr/bin/rancher-exec
ENTRYPOINT ["/sbin/tini","--","/opt/jobber/docker-entrypoint.sh"]
CMD ["jobberd"]

