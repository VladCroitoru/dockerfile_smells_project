FROM alpine:latest
MAINTAINER yumin9822 <yumin9822@gmail.com>

RUN apk update && apk add \
	transmission-daemon \
	&& rm -rf /var/cache/apk/* \
	&& mkdir -p /transmission/{download,watch} \
	&& chmod -R 777 /transmission
RUN wget https://github.com/ronggang/transmission-web-control/raw/master/release/tr-control-easy-install.sh -O - | sh

EXPOSE 9091 51413 51413/udp

VOLUME ["/transmission/download"]

CMD [ "/usr/bin/transmission-daemon", "-f", "--allowed", "*.*.*.*", "-g", "/", "--download-dir", "/transmission/download", "-c", "/transmission/watch" ]
