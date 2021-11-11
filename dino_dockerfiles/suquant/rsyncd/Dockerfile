FROM alpine:edge
MAINTAINER George Kutsurua <g.kutsurua@gmail.com>

RUN apk --no-cache add rsync &&\
	rm -rf /var/cache/apk/*

ENTRYPOINT ["/usr/bin/rsync"]
CMD ["--help"]
