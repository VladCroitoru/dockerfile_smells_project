FROM ubuntu:16.04

MAINTAINER AisM <mario.aistleitner@stiwa.com>

COPY handbrake.list /etc/apt/
COPY vdrtranscode_server /etc/init.d/
COPY vdrtranscode_server.pl /usr/local/bin/
COPY docker-entrypoint.sh /

RUN set -x && \
  apt-get update && \
  apt-get dist-upgrade -y && \
  apt-get install -y handbrake-cli liblogfile-rotate-perl libproc-daemon-perl perl-modules perl-base && \
  groupadd -g 132 vdr && \
  useradd -u 120 vdr -g vdr

ENTRYPOINT [ "/docker-entrypoint.sh" ]



