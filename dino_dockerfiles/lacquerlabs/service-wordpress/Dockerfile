FROM lacquerlabs/service-php7:2.0.12

# Wordpress Specific ENV Vars
ENV DB_CHARSET					utf8mb4
ENV DB_COLLATE					utf8_general_ci
ENV WORDPRESS_DB_NAME			setme_WORDPRESS_DB_NAME
ENV WORDPRESS_DB_USER			setme_WORDPRESS_DB_USER
ENV WORDPRESS_DB_PASSWORD		setme_WORDPRESS_DB_PASSWORD
ENV WORDPRESS_DB_HOST			setme_WORDPRESS_DB_HOST
ENV WORDPRESS_AUTH_KEY			setme_WORDPRESS_AUTH_KEY
ENV WORDPRESS_SECURE_AUTH_KEY	setme_WORDPRESS_SECURE_AUTH_KEY
ENV WORDPRESS_LOGGED_IN_KEY		setme_WORDPRESS_LOGGED_IN_KEY
ENV WORDPRESS_NONCE_KEY			setme_WORDPRESS_NONCE_KEY
ENV WORDPRESS_AUTH_SALT			setme_WORDPRESS_AUTH_SALT
ENV WORDPRESS_SECURE_AUTH_SALT	setme_WORDPRESS_SECURE_AUTH_SALT
ENV WORDPRESS_LOGGED_IN_SALT	setme_WORDPRESS_LOGGED_IN_SALT
ENV WORDPRESS_NONCE_SALT		setme_WORDPRESS_NONCE_SALT
ENV WP_DEBUG					false
ENV WP_TABLE_PREFIX				wp2_

# ENV WP_VERSION				4.8.1
ENV WP_VERSION					latest

USER root

# install database and other needed packages for wordpress
# Remove php7-zlib as it now resides in php7
RUN apk --update --no-cache add nginx php7-fpm openssl dumb-init tzdata \
	php7-ctype php7-mysqli php7-curl php7-dom php7-exif \
	php7-ftp php7-gd php7-gmagick php7-iconv \
	php7-imagick php7-json php7-mbstring php7-mysqli \
	php7-openssl php7-posix php7-simplexml php7-sockets \
	php7-ssh2 php7-tokenizer php7-xml php7-xmlreader

# copy wp-config.php to wordpress directory, will be owned by root.
COPY ./configs/wp-config.php /app/wp-config.php

# download and set the user/group pair for wordpress
RUN wget -O /tmp/wordpress.tgz https://wordpress.org/wordpress-${WP_VERSION}.tar.gz && \
	tar -zxvf /tmp/wordpress.tgz --directory /app --strip-components=1 && \
	apk del openssl && \
	rm /tmp/wordpress.tgz && \
	chown -R nginx:www-data /app

USER nginx
