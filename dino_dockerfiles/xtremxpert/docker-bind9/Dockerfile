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
		bind \
		bind-tools \
		ca-certificates \
		dnsmasq \
		inotify-tools \
		mc \
		nano \
		openntpd \
		rsync \
		tar \
		tzdata \
		unzip \
	&& \
	ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
	rm -fr /var/lib/apk/* && \
	rm -rf /var/cache/apk/* && \
 	mkdir /etc/services.d/named && \
	echo '#!/usr/bin/execlineb -P'  >> /etc/services.d/named/run && \
	echo 'named -c /etc/bind/named.conf -f -4 -u named'  >> /etc/services.d/named/run && \
 	mkdir /etc/services.d/log && \
	echo '#!/bin/sh'  >> /etc/services.d/log/run && \
	echo 'exec logutil-service /var/log/named'  >> /etc/services.d/log/run && \
	echo '/var/log/named true nobody,32768:32768 0644 2700' >> /etc/fix-attrs.d/01-named-log

EXPOSE 53 953

VOLUME /etc/bind

ENTRYPOINT ["/init"]
