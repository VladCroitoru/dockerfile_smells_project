FROM alpine:3.12
MAINTAINER Scott Wang <swang@revenuewire.com>

RUN set -x \
	&& addgroup -g 82 -S www-data \
	&& adduser -u 82 -D -S -G www-data www-data

RUN apk --update add apache2 php7 php7-cli php7-apache2 php7-ctype php7-openssl \
        php7-curl php7-apcu php7-json php7-opcache php7-bcmath php7-simplexml php7-xml \
        php7-intl php7-iconv php7-mbstring php7-session php7-common \
        bash

ENV HTTPD_PREFIX /var/src/html
RUN mkdir -p "$HTTPD_PREFIX" \
	&& chown www-data:www-data "$HTTPD_PREFIX"

COPY conf/php.ini /etc/php7/php.ini
COPY conf/httpd.conf /etc/apache2/httpd.conf
COPY index.php /var/src/html
ADD run-http.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/run-http.sh

EXPOSE 80
CMD ["run-http.sh"]
