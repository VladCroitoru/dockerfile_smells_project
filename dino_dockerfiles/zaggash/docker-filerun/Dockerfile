FROM lsiobase/ubuntu:bionic
MAINTAINER zaggash

# environment variables
ARG DEBIAN_FRONTEND="noninteractive"
ENV FILERUN_PATH="/config/www/filerun"

# update apt and install packages
RUN \
	apt-get update && \
	apt-get install -y \
		curl \
		logrotate \
		ca-certificates \
		git \
		nginx \
		openssl \
		unzip \
		mysql-client \
		graphicsmagick \
		imagemagick \
		ffmpeg \
		php7.2 \
		php7.2-fpm \
		php7.2-common \
		php7.2-curl \
		php7.2-mbstring \
		php7.2-mysql \
		php7.2-xml \
		php7.2-zip \
		php7.2-gd \
		php7.2-imagick \
		php7.2-ldap \
		php7.2-opcache && \

	apt-get install -y \
		php7.2-dev && \

# install IonCube
	curl -O https://downloads.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64.tar.gz && \
	tar xvfz ioncube_loaders_lin_x86-64.tar.gz && \
	PHP_EXT_DIR=$(php-config --extension-dir) && \
	cp "ioncube/ioncube_loader_lin_7.2.so" $PHP_EXT_DIR && \
	echo "zend_extension=ioncube_loader_lin_7.2.so" >> /etc/php/7.2/fpm/conf.d/00_ioncube_loader.ini && \
	rm -rf ioncube ioncube_loaders_lin_x86-64.tar.gz && \

# configure nginx
	echo 'fastcgi_param  SCRIPT_FILENAME $document_root$fastcgi_script_name;' >> \
		/etc/nginx/fastcgi_params && \
	rm -f /etc/nginx/conf.d/default.conf && \

# cleanup
	apt-get autoremove --purge -y \
		php7.2-dev && \
	rm -rf \
		/tmp/* \
		/var/lib/apt/lists/* \
		/var/tmp/* \
		/usr/lib/x86_64-linux-gnu/libfakeroot/ \
		/etc/logrotate.d/php7.2-fpm \
		/etc/logrotate.d/nginx

# add local files
COPY root/ /

# ports and volumes
EXPOSE 80
VOLUME /config
