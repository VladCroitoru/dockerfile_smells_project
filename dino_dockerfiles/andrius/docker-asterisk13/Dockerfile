# vim:set ft=dockerfile:
FROM debian:stable-slim

MAINTAINER Andrius Kairiukstis <andrius@kairiukstis.com>

RUN apt-get -yqq update \
&&  apt-get -yqq --no-install-recommends --no-install-suggests install \
      procps \
      asterisk \
      asterisk-config \
      asterisk-core-sounds-en \
      asterisk-core-sounds-en-gsm \
      asterisk-moh-opsound-gsm \
&&  ln -s /usr/share/asterisk/sounds/en /var/lib/asterisk/sounds/en \
&&  asterisk \
&&  sleep 5 \
&&  pkill -9 asterisk \
&&  apt-get -yqq purge procps \
&&  apt-get clean all \
&&  rm -rf /var/lib/apt/lists/* /usr/share/doc /usr/share/man* /tmp/* /var/tmp/*

ADD docker-entrypoint.sh /docker-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["/usr/sbin/asterisk", "-vvvdddf", "-T", "-W", "-U", "root", "-p"]

