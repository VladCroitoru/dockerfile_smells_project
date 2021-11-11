FROM adminer as base

FROM php:7.2-apache-stretch

STOPSIGNAL SIGINT

RUN set -x && \
    apt-get update && \
    apt-get install -y libpq-dev libsqlite3-dev libapache2-mod-auth-cas  && \
    docker-php-ext-configure pgsql -with-pgsql=/usr/local/pgsql && \ 
    docker-php-ext-install pdo_mysql pdo_pgsql pdo_sqlite && \
    rm -rf /var/lib/apt/lists/*

COPY --from=base /var/www/html/ /var/www/html/
COPY auth_cas.conf /etc/apache2/mods-enabled/auth_cas.conf
COPY index.php adminer.css ./
