FROM alpine:latest

RUN set -xe \
	&& apk add --update --no-cache dhcrelay tzdata \
	&& rm -rf /var/cache/apk/*

ADD entrypoint.sh /entrypoint.sh
ENTRYPOINT [ "/entrypoint.sh" ]
