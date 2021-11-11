FROM alpine:3.6
MAINTAINER Giuseppe Pellegrino <g.pellegrino@tadaweb.com>

RUN apk update && \
    apk add lighttpd php5-common php5-gd php5-curl php5-pgsql php5-cgi fcgi php5-pdo php5-pdo_pgsql php5-dom php5-pgsql postgresql-client && \
    apk add bash wget postgresql postgresql-client && rm -rf /var/cache/apk/*

RUN wget http://downloads.sourceforge.net/phppgadmin/phpPgAdmin-5.0.4.tar.gz && \
    tar -xzf phpPgAdmin-5.0.4.tar.gz && rm phpPgAdmin-5.0.4.tar.gz && \
    mv phpPgAdmin-5.0.4 /var/www/localhost/phppgadmin && \
    chown -R lighttpd:lighttpd /var/www/localhost/phppgadmin && chmod -R 777 /var/www/localhost/phppgadmin

RUN mkdir -p /var/run/lighttpd && touch /var/run/lighttpd/php-fastcgi.socket && chown -R lighttpd:lighttpd /var/run/lighttpd

COPY lighttpd.conf /etc/lighttpd/lighttpd.conf
COPY mod_fastcgi.conf /etc/lighttpd/mod_fastcgi.conf
COPY config.inc.php /var/www/localhost/phppgadmin/conf/config.inc.php

RUN chmod +x /var/www/localhost/phppgadmin/conf/config.inc.php

ENV POSTGRESQL_SSL_MODE allow
ENV PHPPGADMIN_PORT 8060
#ENV POSTGRESQL_DEFAULT_DB defaultdb
# comma separated list of nodes
ENV POSTGRESQL_HOSTS localhost:5432

CMD ["lighttpd", "-D", "-f", "/etc/lighttpd/lighttpd.conf"]
