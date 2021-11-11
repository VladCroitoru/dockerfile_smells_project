FROM alpine:3.3
MAINTAINER George Kutsurua <g.kutsurua@gmail.com>

RUN apk update && \
 	apk add bash less vim nginx ca-certificates \
    	php-fpm php-json php-zlib php-xml php-pdo php-phar php-openssl php-zip \
    	php-pdo_mysql php-mysqli \
    	php-gd php-iconv php-mcrypt \
    	php-mysql php-curl php-opcache php-ctype php-apcu \
    	php-intl php-bcmath php-dom php-xmlreader mysql-client musl curl && \
    rm -rf /var/cache/apk/* && \
    sed -i 's/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g' /etc/php/php.ini

ADD nginx.conf /etc/nginx/
ADD php-fpm.conf /etc/php/
ADD entrypoint.sh /entrypoint.sh

EXPOSE 80
VOLUME ["/data"]

ENTRYPOINT ["/entrypoint.sh"]
CMD [""]