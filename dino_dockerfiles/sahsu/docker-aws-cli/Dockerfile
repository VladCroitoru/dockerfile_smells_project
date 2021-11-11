FROM alpine:latest

RUN \
	mkdir -p /aws && \
	apk -Uuv add groff less python py-pip && \
	pip install --upgrade awscli && \
	apk --purge -v del py-pip && \
	rm /var/cache/apk/*

WORKDIR /aws
ENTRYPOINT ["aws"]
