FROM alpine:3.4
MAINTAINER Chris <clbatis@taosnet.com>

RUN apk update && \
	apk add rsync openssh openssh-client nmap nmap-ncat jq && \
	rm -rf /var/cache/apk/*
CMD ["-a", "/source", "/dest"]
ENTRYPOINT ["/usr/bin/rsync"]
