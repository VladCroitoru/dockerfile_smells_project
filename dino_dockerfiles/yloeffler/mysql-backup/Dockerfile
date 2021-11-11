FROM alpine:latest
LABEL maintainer="Yohann LOEFFLER <loeffler.yohann@pm.me>"

RUN apk add --no-cache \
        mysql-client \
    ; \
    mkdir /backup

ENV COMPRESS_CMD="gzip" \
    CRON_TIME="0 0 * * *" \
    MYSQL_DB="--all-databases"
ADD run.sh /run.sh
VOLUME ["/backup"]

ENTRYPOINT ["/run.sh"]
CMD ["/usr/sbin/crond", "-l 2", "-f"]
