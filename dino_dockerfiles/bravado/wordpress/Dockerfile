FROM bravado/php:7.3

ARG WP_VERSION=5.4.1

RUN curl -L https://br.wordpress.org/wordpress-${WP_VERSION}-pt_BR.tar.gz | tar -xz -C /var/www/html

USER root

ADD etc/ /etc/
ADD src/ /var/www/

ENV \
APACHE_RUN_USER=app \
APACHE_RUN_GROUP=app \
WP_DB_NAME=wordpress \
WP_DB_USER=wordpress \
WP_DB_PASSWORD=wordpress \
WP_DB_HOST=mysql \
WP_DB_CHARSET=utf8mb4 \
WP_DB_COLLATE=

VOLUME /var/www/html/wp-content

USER app
