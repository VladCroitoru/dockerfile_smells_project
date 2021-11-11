FROM xtremxpert/docker-alpine:latest

MAINTAINER Xtremxpert <xtremxpert@xtremxpert.com>

ENV MAX_UPLOAD "50M"

RUN apk -U upgrade && \
	apk --update add \
		apache2 \
		apache2-utils \
		php-apache2 \
		php-cli \
		php-ctype \
		php-curl \
		php-exif \
		php-gd \
		php-json \
		php-mysqli \
		php-opcache \
		php-openssl \
		php-phar \
		php-xml \
		php-zip \
		php-zlib \
	&& \
	sed -i 's#AllowOverride none#AllowOverride All#' /etc/apache2/httpd.conf && \
	sed -i 's#^DocumentRoot ".*#DocumentRoot "/var/www/htdocs"#g' /etc/apache2/httpd.conf && \
	sed -i 's#output_buffering = 4096#output_buffering = Off#' /etc/php/php.ini && \
	sed -i \
		-e "s/^upload_max_filesize\s*=\s*2M/upload_max_filesize = $MAX_UPLOAD/" \
		-e "s/^post_max_size\s*=\s*8M/post_max_size = $MAX_UPLOAD/" \
		/etc/php/php.ini \
	&& \
	mv /var/www/localhost /var/www/ && \
	rm -rf /var/cache/apk/*

ADD files/test.php /var/www/htdocs/

EXPOSE 80
EXPOSE 443

ENTRYPOINT ["/usr/sbin/httpd"]
CMD ["-DFOREGROUND"]

#CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
#ENTRYPOINT [ "httpd -D FOREGROUND" ]
