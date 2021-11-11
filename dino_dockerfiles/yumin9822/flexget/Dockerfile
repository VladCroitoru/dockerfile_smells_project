FROM alpine:latest
MAINTAINER yumin9822 <yumin9822@gmail.com>

RUN apk update && apk add wget python \
	&& rm -rf /var/cache/apk/* \
	&& wget --no-check-certificate https://bootstrap.pypa.io/get-pip.py -O - | python

RUN pip install -I pytest-runner \
	&& pip install -I flexget transmissionrpc \
	&& mkdir -p /root/.flexget \
	&& touch /root/.flexget/config.yml

VOLUME ["/root/.flexget"]

CMD ["/usr/bin/flexget", "--loglevel", "info", "daemon", "start"]
