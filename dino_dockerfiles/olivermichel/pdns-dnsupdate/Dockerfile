
FROM  alpine:3.10

MAINTAINER Oliver Michel <oliver.michel@editum.de>

COPY assets/schema.sql /etc/pdns/schema.sql
COPY assets/entrypoint.sh /root/entrypoint.sh

VOLUME ["/srv/pdns"]

EXPOSE 53/tcp 53/udp

RUN apk --no-cache add pdns pdns-backend-sqlite3 sqlite \
    && rm /etc/pdns/pdns.conf  \
    && mkdir -p /var/empty/var/run/ \
    && chmod u+x /root/entrypoint.sh

ENTRYPOINT [ "/root/entrypoint.sh" ]
