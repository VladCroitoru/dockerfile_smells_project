FROM linuxserver/letsencrypt:latest
LABEL maintainer "T Koopman"

RUN apk add --no-cache \
        php7-pdo_sqlite \
        php7-sqlite3 \
        php7-zip

COPY root/ /

RUN chmod +x /etc/cont-init.d/40-*