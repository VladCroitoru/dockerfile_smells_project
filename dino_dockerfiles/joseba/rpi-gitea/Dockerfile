FROM resin/armhf-alpine:latest

LABEL maintainer="joseba.io"

EXPOSE 22 3000

ENV VERSION 1.2.2

RUN [ "cross-build-start" ]

RUN apk --no-cache add \
    su-exec \
    ca-certificates \
    sqlite \
    bash \
    git \
    linux-pam \
    s6 \
    curl \
    openssh \
    gettext \
    subversion \
    tzdata
RUN addgroup \
    -S -g 1000 \
    git && \
  adduser \
    -S -H -D \
    -h /data/git \
    -s /bin/bash \
    -u 1000 \
    -G git \
    git && \
  echo "git:$(dd if=/dev/urandom bs=24 count=1 status=none | base64)" | chpasswd

ENV USER git
ENV GITEA_CUSTOM /data/gitea
ENV GODEBUG=netdns=go

RUN svn export https://github.com/go-gitea/gitea/trunk/docker ./ --force

RUN mkdir -p /app/gitea && \
    curl -SLo /app/gitea/gitea https://github.com/go-gitea/gitea/releases/download/v$VERSION/gitea-$VERSION-linux-arm-7 && \
chmod 0755 /app/gitea/gitea

RUN [ "cross-build-end" ]

VOLUME ["/data"]

ENTRYPOINT ["/usr/bin/entrypoint"]
CMD ["/bin/s6-svscan", "/etc/s6"]


