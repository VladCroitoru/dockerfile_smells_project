FROM	alpine:3.8
MAINTAINER Carsten Ringe <carsten@kopis.de>

EXPOSE	80
VOLUME	["/dokuwiki-data", "/dokuwiki-conf", "/dokuwiki-plugins"]
ARG	VERSION=dokuwiki-2020-07-29
ENV	VERSION=$VERSION

RUN	apk update && apk add -U php5-cli php5-mysqli php5-ctype php5-xml php5-gd php5-zlib php5-openssl php5-curl php5-opcache php5-json php5-ldap curl

ADD	docker-entrypoint.sh /docker-entrypoint.sh

CMD	["/docker-entrypoint.sh"]
