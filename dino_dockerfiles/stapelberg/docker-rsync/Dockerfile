FROM debian:jessie
MAINTAINER Michael Stapelberg <michael+nas@stapelberg.ch>

RUN apt-get update \
    && apt-get install -y rsync \
    && gunzip -c /usr/share/doc/rsync/scripts/rrsync.gz > /usr/bin/rrsync \
    && chmod +x /usr/bin/rrsync

ENTRYPOINT ["/usr/bin/rrsync"]
