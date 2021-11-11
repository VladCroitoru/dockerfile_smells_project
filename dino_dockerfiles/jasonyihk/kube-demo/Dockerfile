FROM php:7.1-fpm

# Install required libs by docker-php-ext-install
RUN apt-get update && apt-get install -y --no-install-recommends \
    apache2 \
    git zip unzip \
    libmcrypt-dev \
    libxml++2.6-dev \
    python python-dev python-pip \
    webp libjpeg-dev libpng-dev \
    supervisor \
    && docker-php-ext-install opcache mcrypt mbstring xml \
    && rm -rf /var/lib/apt/lists/*

ENV APACHE_CONFDIR /etc/apache2
ENV APACHE_ENVVARS $APACHE_CONFDIR/envvars

RUN set -ex \
# generically convert lines like
#   export APACHE_RUN_USER=www-data
# into
#   : ${APACHE_RUN_USER:=www-data}
#   export APACHE_RUN_USER
# so that they can be overridden at runtime ("-e APACHE_RUN_USER=...")
	&& sed -ri 's/^export ([^=]+)=(.*)$/: ${\1:=\2}\nexport \1/' "$APACHE_ENVVARS" \
# setup directories and permissions
	&& . "$APACHE_ENVVARS" \
	&& for dir in \
		"$APACHE_LOCK_DIR" \
		"$APACHE_RUN_DIR" \
		"$APACHE_LOG_DIR" \
		/var/www/html \
	; do \
		rm -rvf "$dir" \
		&& mkdir -p "$dir" \
		&& chown -R "$APACHE_RUN_USER:$APACHE_RUN_GROUP" "$dir"; \
	done

# logs should go to stdout / stderr
RUN set -ex \
	&& . "$APACHE_ENVVARS" \
	&& ln -sfT /dev/stderr "$APACHE_LOG_DIR/error.log" \
	&& ln -sfT /dev/stdout "$APACHE_LOG_DIR/access.log" \
	&& ln -sfT /dev/stdout "$APACHE_LOG_DIR/other_vhosts_access.log"

# PHP files should be handled by PHP, and should be preferred over any other file type
RUN { \
		echo '<FilesMatch \.php$>'; \
		echo '\tSetHandler application/x-httpd-php'; \
		echo '</FilesMatch>'; \
		echo; \
		echo 'DirectoryIndex disabled'; \
		echo 'DirectoryIndex index.php index.html'; \
		echo; \
		echo '<Directory /var/www/>'; \
		echo '\tOptions -Indexes'; \
		echo '\tAllowOverride All'; \
		echo '</Directory>'; \
	} | tee "$APACHE_CONFDIR/conf-available/docker-php.conf" \
	&& a2enconf docker-php

# Install composer
RUN curl -sS https://getcomposer.org/installer | \
    php -- --install-dir=/usr/local/bin --filename=composer

# Install web-converter to convert png/jpg to webp
RUN pip install webp-converter

# Remove default site conf in Debian
RUN rm /etc/apache2/sites-enabled/000-default.conf

RUN a2enmod rewrite headers mime
RUN a2dismod mpm_prefork mpm_worker
RUN a2enmod proxy proxy_fcgi mpm_event

# Copy site conf
COPY config/httpd.conf /etc/apache2/sites-enabled/web.conf
# Copy custom php.ini
COPY config/php.ini /usr/local/etc/php/php.ini
# Copy custome php-fpm pool conf
COPY config/zz-docker.conf /usr/local/etc/php-fpm.d/zz-docker.conf
COPY config/www.conf /usr/local/etc/php-fpm.d/www.conf

# Copy custom php.ini
COPY config/php.ini /usr/local/etc/php/php.ini
# Copy custome php-fpm pool conf
COPY config/www.conf /etc/php5/fpm/pool.d/www.conf

# Copy src code
COPY src/ /var/www/html

# Install required package by composer.json
RUN cd /var/www/html && composer install

RUN cp -rp /var/www/html/public/img /var/www/html/public/img_bk
# Replace the png/jpg to webp if webp file is smaller
# We use 75 quality and it look good in image quality, encode speed and file size
RUN webpc -q 75 --r /var/www/html/public/img/
# Restore deleted png/jpg back
RUN cp -rpn /var/www/html/public/img_bk/* /var/www/html/public/img
RUN rm -rf /var/www/html/public/img_bk

COPY apache2-foreground /usr/local/bin/
COPY supervisord.conf /etc/supervisor/supervisord.conf
COPY ./docker-entrypoint.sh /

ENTRYPOINT ["/docker-entrypoint.sh"]
RUN chmod +x /usr/local/bin/apache2-foreground
RUN chmod +x /docker-entrypoint.sh

EXPOSE 80

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]
