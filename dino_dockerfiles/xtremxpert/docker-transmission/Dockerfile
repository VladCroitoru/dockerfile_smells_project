FROM alpine:edge

MAINTAINER XtremXpert <xtremxpert@xtremxpert.com>

ENV LANG="fr_CA.UTF-8" \
	LC_ALL="fr_CA.UTF-8" \
	LANGUAGE="fr_CA.UTF-8" \
	TZ="America/Toronto" \
	TERM="xterm" \
	TRANSMISSION_HOME="/transmission/config"

ADD https://github.com/just-containers/s6-overlay/releases/download/v1.11.0.1/s6-overlay-amd64.tar.gz /tmp/

RUN apk update && \
	apk update && \
	apk add \
		ca-certificates \
		mc \
		nano \
		openntpd \
		rsync \
		transmission-daemon \
		tzdata \
		unzip \
	&& \
	tar xzf /tmp/s6-overlay-amd64.tar.gz -C / && \
	echo "@testing http://dl-4.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories && \
	mkdir -p /transmission/{download,watch,incomplete,config} && \
	chmod 1777 /transmission && \
	ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
	rm -fr /var/lib/apk/* && \
	rm -rf /var/cache/apk/*

EXPOSE 9091

ENTRYPOINT ["/init"]

CMD ["/usr/bin/transmission-daemon","--allowed", "127.*,10.*,192.168.*,172.16.*,172.17.*,172.18.*,172.19.*,172.20.*,172.21.*,172.22.*,172.23.*,172.24.*,172.25.*,172.26.*,172.27.*,172.28.*,172.29.*,172.30.*,172.31.*,169.254.*", "--watch-dir", "/transmission/watch", "--encryption-preferred", "--foreground", "--config-dir", "/transmission/config", "--incomplete-dir", "/transmission/incomplete", "--dht", "--no-auth", "--download-dir", "/transmission/download" ]
