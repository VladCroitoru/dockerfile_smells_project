FROM wordpress

RUN apt-get update && apt-get install -y ssmtp libfreetype6-dev libjpeg-dev \
	&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr --with-freetype-dir=/usr \
	&& docker-php-ext-install gd

RUN touch /usr/local/etc/php/conf.d/uploads.ini \
	&& echo "post_max_size = 50M;" >> /usr/local/etc/php/conf.d/uploads.ini \
	&& echo "upload_max_filesize = 50M;" >> /usr/local/etc/php/conf.d/uploads.ini

RUN touch /usr/local/etc/php/conf.d/ssmtp.ini \
	&& echo "[mail function]" >> /usr/local/etc/php/conf.d/ssmtp.ini \
	&& echo "sendmail_path = /usr/sbin/ssmtp -t;" >> /usr/local/etc/php/conf.d/ssmtp.ini
