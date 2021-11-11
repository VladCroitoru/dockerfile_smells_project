FROM frolvlad/alpine-glibc

MAINTAINER Axel Henry <axel.durandil@gmail.com>

ENV DBOX_UID 1000
ENV DBOX_GID 1000
ENV PATH /opt/dropbox:$PATH
ENV S6_VERSION 1.20.0.0

USER root

#Download s6-overlay's files
ADD https://keybase.io/justcontainers/key.asc /tmp/key.asc
ADD https://github.com/just-containers/s6-overlay/releases/download/v$S6_VERSION/s6-overlay-amd64.tar.gz /tmp/s6.tar.gz
ADD https://github.com/just-containers/s6-overlay/releases/download/v$S6_VERSION/s6-overlay-amd64.tar.gz.sig /tmp/s6.sig

#Download dropbox's files
#testing autoupdate by downloading an old version
#ADD https://d1ilhw0800yew8.cloudfront.net/client/dropbox-lnx.x86_64-12.4.22.tar.gz /tmp/dropbox-linux-x86_64.tar.gz
#ADD https://www.dropbox.com/download?plat=lnx.x86_64 /tmp/dropbox-linux-x86_64.tar.gz
ADD https://www.dropbox.com/download?dl=packages/dropbox.py /usr/local/bin/dropbox-cli

#cloudfront not working right now, so copy dropbox from a local archive
COPY dropbox.x86_64-11.4.20.tar.gz /tmp/dropbox-linux-x86_64.tar.gz
#COPY repositories /etc/apk/repositories

RUN set -xe \
    && apk --no-cache add python tar gnupg curl

#Verify s6-overlay' signature
RUN set -xe \
    && cd /tmp \
    && gpg --import /tmp/key.asc \
    && gpg --verify /tmp/s6.sig /tmp/s6.tar.gz \
    && tar xzf s6.tar.gz -C /

RUN set -xe \
    && mkdir -p /opt/dropbox \
    && tar xzfv /tmp/dropbox-linux-x86_64.tar.gz --strip 1 -C /opt/dropbox

#Delete /tmp folder content
RUN set -xe \
    && rm -rf /tmp/* /root/.gnupg

RUN set -xe \
    && apk --no-cache del gnupg tar

WORKDIR /home/dbox

EXPOSE 17500

VOLUME ["/home/dbox/Dropbox", "/home/dbox/.dropbox"]

#fix files and folders permissions
COPY dropbox.fixattrs.s6 /etc/fix-attrs.d/00-dropbox
COPY dropbox-cli.fixattrs.s6  /etc/fix-attrs.d/01-dropbox-cli
COPY cron.fixattrs.s6 /etc/fix-attrs.d/02-cron-scripts

#preinit scripts
COPY create-user.s6 /etc/cont-init.d/01-create-user.sh
COPY create-user-folders.s6 /etc/cont-init.d/02-create-user-folders.sh
COPY display-dropbox-version.s6 /etc/cont-init.d/04-display-dropbox-version.sh

#services
#   dropbox service
COPY dropbox-user.service.s6 /etc/services.d/dropbox@dbox/run
#   launch crond and cron file
COPY cron.service.s6 /etc/services.d/cron/run
#COPY dropbox-updater.s6 /etc/periodic/15min/check_dropboxd_update
COPY dropbox-updater.s6 /etc/periodic/daily/check_dropboxd_update



ENTRYPOINT ["/init"]
