FROM alpine:edge

MAINTAINER XtremXpert <xtremxpert@xtremxpert.com>

ENV LANG="fr_CA.UTF-8" \
	LC_ALL="fr_CA.UTF-8" \
	LANGUAGE="fr_CA.UTF-8" \
	TZ="America/Toronto" \
	TERM="xterm"

ADD https://github.com/just-containers/s6-overlay/releases/download/v1.11.0.1/s6-overlay-amd64.tar.gz /tmp/

RUN tar xzf /tmp/s6-overlay-amd64.tar.gz -C / && \
	echo "@testing http://dl-4.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories && \
	apk update && \
	apk upgrade && \
	apk add \
		asterisk \
		asterisk-sample-config \
		ca-certificates \
		fcgi \
		lighttpd \
		mc \
		nano \
		openntpd \
		patch \
		perl \
		php-common \
		php-cgi \
		php-curl \
		php-ctype \
		php-dom \
		php-iconv \
		php-imap \
		php-gd \
		php-gettext \
		php-json \
		php-ldap \
		php-mcrypt \
		mariadb \
		mariadb-client \
		php-pdo \
		php-pdo_pgsql \
		php-pear \
		php-pgsql \
		php-posix \
		php-soap \
		php-xml  \
		php-xmlrpc \
		rsync \
		sed \
		tar \
		tzdata \
		unzip \
	&& \
	ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
	rm -fr /var/lib/apk/* && \
	rm -rf /var/cache/apk/* && \
# 	mkdir /etc/services.d/asterisk && \
#	echo '#!/usr/bin/execlineb -P'  >> /etc/services.d/asterisk/run && \
#	echo 'asterisk'  >> /etc/services.d/asterisk/run && \
 	mkdir /etc/services.d/mysql && \
	echo '#!/usr/bin/execlineb -P'  >> /etc/services.d/mysql/run && \
	echo 'mysqld --user=mysql'  >> /etc/services.d/mysql/run && \
 	mkdir /etc/services.d/lighttpd && \
	echo '#!/usr/bin/execlineb -P'  >> /etc/services.d/lighttpd/run && \
	echo 'lighttpd -D -f /etc/lighttpd/lighttpd.conf'  >> /etc/services.d/lighttpd/run

EXPOSE 80 443 5060

ENTRYPOINT ["/init"]
