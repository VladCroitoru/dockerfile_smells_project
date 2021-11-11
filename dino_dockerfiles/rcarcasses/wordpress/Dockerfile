FROM wordpress

# mbstring is needed by some plugins
RUN docker-php-ext-install mbstring zip

# just some freedom
RUN touch /usr/local/etc/php/conf.d/uploads.ini \
	&& echo "post_max_size = 120M;" >> /usr/local/etc/php/conf.d/uploads.ini \
	&& echo "upload_max_filesize = 120M;" >> /usr/local/etc/php/conf.d/uploads.ini
