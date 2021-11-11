FROM debian:jessie
MAINTAINER Hellyna NG <hellyna@groventure.com>

COPY scripts/* /scripts/
COPY conf/* /usr/local/etc/rattic/
RUN bash /scripts/build.sh

EXPOSE 8000/tcp
VOLUME ["/srv/rattic"]
WORKDIR /srv/rattic

ENTRYPOINT ["bash", "/scripts/entrypoint.sh"]
