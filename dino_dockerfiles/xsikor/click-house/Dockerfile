FROM ubuntu:14.04

MAINTAINER xsikor

EXPOSE 8123

ENV TERM=xterm

RUN mkdir -p /etc/apt/sources.list.d \
	&& echo "deb http://repo.yandex.ru/clickhouse/trusty/ dists/stable/main/binary-amd64/" > /etc/apt/sources.list.d/clickhouse.list \
	&& apt-get update

RUN apt-get install -y --allow-unauthenticated clickhouse-server-common clickhouse-client

CMD ["clickhouse-server", "--config-file", "/etc/clickhouse-server/config.xml"]