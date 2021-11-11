FROM alpine:latest
MAINTAINER WangXian <xian366@126.com>

WORKDIR /app
VOLUME /app
COPY startup.sh /startup.sh

RUN apk add --update mysql mysql-client && rm -f /var/cache/apk/*
COPY mysql-plugins/calc_distance_udf.so /usr/lib/mysql/plugin/calc_distance_udf.so
COPY my.cnf /etc/mysql/my.cnf

EXPOSE 3306
CMD ["/startup.sh"]
