FROM alpine
MAINTAINER sahsu.mobi@gmail.com

RUN \
	mkdir -p /aws && \
	apk -Uuv add groff less python py-pip && \
	pip install saws && \
	apk --purge -v del py-pip && \
	rm /var/cache/apk/*

WORKDIR /aws
ENTRYPOINT ["saws"]
