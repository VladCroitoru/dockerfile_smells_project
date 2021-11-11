FROM alpine:3.14
LABEL name="powerdns" version="4.4.1" maintainers="Sebastian Pitsch <pitsch@freinet.de>, Dominic Zöller <zoeller@freinet.de>"
# Based on https://hub.docker.com/r/psitrax/powerdns/

ENV MYSQL_DEFAULT_AUTOCONF=true \
    MYSQL_DEFAULT_HOST="mysql" \
    MYSQL_DEFAULT_PORT="3306" \
    MYSQL_DEFAULT_USER="root" \
    MYSQL_DEFAULT_PASS="root" \
    MYSQL_DEFAULT_DB="pdns"

RUN apk add --no-cache \
    bash=5.1.4-r0 \
    mariadb-client=10.5.12-r0 \
    pdns=4.4.1-r6 \
    pdns-backend-mariadb=4.4.1-r6 && \
    mkdir -p /etc/pdns/conf.d && \
    rm -rf /var/cache/apk/*

COPY schema.sql pdns.conf /etc/pdns/
COPY entrypoint.sh /

EXPOSE 53/tcp 53/udp

ENTRYPOINT ["/entrypoint.sh"]
