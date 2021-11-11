FROM alpine
MAINTAINER Chris Batis <clbatis@taosnet.com>

RUN apk --no-cache add dropbear-scp dropbear-dbclient

ENTRYPOINT ["/usr/bin/scp"]
