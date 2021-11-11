FROM alpine:latest
MAINTAINER Gunnar Falk <docker@grundstil.de>
# Based on kost/docker-alpine/alpine-mariadb
# and https://github.com/christiansteier/dockerfiles-rpi/tree/master/alpine-mysql

ENV LANG="en_US.UTF-8" \
    LC_ALL="en_US.UTF-8" \
    LANGUAGE="en_US.UTF-8" \
    DB_USER="admin" \
    DB_PASS="password" \
    TERM="xterm"

RUN apk -U upgrade && \
    apk --update add \
      mariadb mariadb-server-utils mariadb-client mariadb-backup \
      && \
      rm -rf /tmp/src && \
      rm -rf /var/cache/apk/*

ADD ./files/my.cnf /etc/mysql/my.cnf
ADD ./files/start.sh /start.sh

RUN chmod u+x /start.sh

VOLUME ["/data"]
EXPOSE 3306
CMD ["/start.sh"]
