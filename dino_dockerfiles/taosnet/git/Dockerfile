FROM alpine:3.4
MAINTAINER Chris Batis <clbatis@taosnet.com>

RUN apk update && \
	apk add git && \
	rm -rf /var/cache/apk/* && \
	mkdir /git

WORKDIR /git

ENTRYPOINT ["/usr/bin/git"]
