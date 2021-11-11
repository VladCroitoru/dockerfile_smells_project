FROM alpine:edge
MAINTAINER George Kutsurua <g.kutsurua@gmail.com>

RUN apk --update add mariadb mariadb-client pwgen && \
    rm -f /var/cache/apk/*

ADD entrypoint.sh /entrypoint.sh

EXPOSE 3306
VOLUME ["/var/lib/mysql"]

ENTRYPOINT ["/entrypoint.sh"]
CMD ["--user=mysql", "--console"]
