FROM alpine:3.4
MAINTAINER Chris Batis <clbatis@taosnet.com>

RUN apk update && \
        apk add mariadb mariadb-client && \
        rm -rf /var/cache/apk/* && \
	mkdir /docker-entrypoint-initdb.d

EXPOSE 3306

COPY run.sh /run.sh
ENTRYPOINT ["/run.sh"]
