FROM alpine:latest

MAINTAINER Dmitry Karikh <the.dr.hax@gmail.com>

RUN apk --no-cache add mysql-client pigz

COPY backup /usr/local/bin/

ENV PROFILES="" \
    RETENTION_PERIOD="7" \
    MYSQLDUMP_OPTIONS="--lock-tables"

VOLUME /backup
WORKDIR /backup
CMD ["backup"]
