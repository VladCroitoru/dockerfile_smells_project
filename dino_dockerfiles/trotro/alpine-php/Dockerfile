FROM alpine

# Install PHP
RUN apk update \
	&& apk add \
	php-common php-mcrypt php-soap php-xmlreader \
	php-curl php-intl php-zlib \
	php-enchant php-zip php-dom php-gettext \
	php-mysql php-mysqli php-pear php-pdo_mysql php-json \
	php-pdo php-gd php-openssl php-iconv \
	php-xml php-xsl php-fpm php-ctype \
	&& rm -rf /var/cache/apk/* \
	# forward request and error logs to docker log collector
	&& ln -sf /dev/stdout /var/log/php-fpm.log

# Set the locale
#RUN locale-gen en_US.UTF-8
#RUN locale-gen fr_FR.UTF-8
#ENV LANG en_US.UTF-8
#ENV LANGUAGE en_US:en
#ENV LC_ALL en_US.UTF-8

EXPOSE 9000

CMD ["php-fpm","-F"]
