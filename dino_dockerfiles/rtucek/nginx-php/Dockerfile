FROM debian:jessie

ARG BUILD_DATE
ARG VCS_REF
ARG VERSION

LABEL \
	org.label-schema.build-date=${BUILD_DATE} \
	org.label-schema.name="nginx-php Dockerfile" \
	org.label-schema.schema-version="1.0" \
	org.label-schema.vcs-ref=${VCS_REF} \
	org.label-schema.vcs-url="https://github.com/rtucek/nginx-php" \
	org.label-schema.version=${VERSION}

ENV \
	NGINX_VERSION=1.13.1 \
	PHP_VERSION=7.1.6 \
	XDEBUG_VERSION=2.5.4 \
	VERSION=${VERSION}

COPY \
	docker-entrypoint \
	fix-permission \
	nginx.conf \
	Procfile \
	/tmp/build/scripts/

RUN \
	# Install tools, required for building
	apt-get update && \
	apt-get install -y --no-install-recommends \
		# For building (will be removed)
		autoconf \
		build-essential \
		curl \

		# For Nginx
		libpcre3-dev \
		libssl-dev \

		# For PHP
		bison \
		libbz2-dev \
		libcurl4-openssl-dev \
		libpng12-dev \
		libpq-dev \
		libreadline-dev \
		libxml2-dev \
		libxslt1-dev \
		pkg-config \
		re2c \

		# For PHP composer
		git \

		# For Honcho
		python \
		python-pip \
		python-pkg-resources \

		# Fron crontab
		cron && \

	pip install honcho && \

	# Prepare for building
	mkdir -p /tmp/build && \

	mkdir -p /tmp/build/nginx/ && \
	cd /tmp/build/nginx && \

	# Download Nginx
	curl -SLO https://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz && \

	cd /tmp/build/nginx && \

	# GPG keys from the main maintainers of Nginx
	# Source https://nginx.org/en/pgp_keys.html
	gpg --keyserver sks-keyservers.net --recv-keys \
		"6550 6C02 EFC2 50F1 B7A3  D694 ECF0 E90B 2C17 2083" \
		"4C2C 85E7 05DC 7308 3399  0C38 A937 6139 A524 C53E" \
		"B0F4 2533 73F8 F6F5 10D4  2178 520A 9993 A1C0 52F8" \
		"7338 9730 69ED 3F44 3F4D  37DF A64F D5B1 7ADB 39A8" \
		"A09C D539 B8BB 8CBE 96E8  2BDF ABD4 D3B3 F580 6B4D" \
		"573B FD6B 3D8F BC64 1079  A6AB ABF5 BD82 7BD9 BF62" && \

	# Verify signature
	curl -SLO https://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz.asc && \
	gpg nginx-${NGINX_VERSION}.tar.gz.asc && \

	cd /tmp/build/nginx && \
	# Unpack tarball
	tar -xvzf nginx-${NGINX_VERSION}.tar.gz && \

	cd /tmp/build/nginx/nginx-${NGINX_VERSION} && \
	# Run configuration
	./configure \
		--group=www-data \
		--user=www-data \
		--with-file-aio \
		--with-http_gunzip_module \
		--with-http_gzip_static_module \
		--with-http_realip_module \
		--with-http_ssl_module \
		--with-http_v2_module \
		--with-pcre \
		--with-threads && \

	cd /tmp/build/nginx/nginx-${NGINX_VERSION} && \
	# Start compiling and installing
	make -j$(nproc) build && \
	make modules && \
	make install && \

	# Nginx configuration
	mv /tmp/build/scripts/nginx.conf /usr/local/nginx/conf/ && \

	mkdir -p /tmp/build/php/ && \
	cd /tmp/build/php && \

	# Download PHP
	curl -SLo php-${PHP_VERSION}.tar.gz http://ch1.php.net/get/php-${PHP_VERSION}.tar.gz/from/this/mirror && \

	cd /tmp/build/php/ && \

	# GPG keys from the release managers of PHP 7.1
	# Source https://secure.php.net/downloads.php#gpg-7.1
	gpg --keyserver sks-keyservers.net --recv-keys \
		"A917 B1EC DA84 AEC2 B568 FED6 F50A BC80 7BD5 DCD0" \
		"5289 95BF EDFB A719 1D46 839E F9BA 0ADA 31CB D89E" && \

	# Verify signature
	curl -SLo php-${PHP_VERSION}.tar.gz.asc http://ch1.php.net/get/php-${PHP_VERSION}.tar.gz.asc/from/this/mirror && \
	gpg php-${PHP_VERSION}.tar.gz.asc && \

	cd /tmp/build/php && \
	# Unpack tarball
	tar -xvzf php-${PHP_VERSION}.tar.gz && \

	cd /tmp/build/php/php-${PHP_VERSION} && \
	# Run configuration
	./configure \
		--enable-fpm \
		--enable-mbregex \
		--enable-mbstring=all \
		--enable-opcache \
		--enable-sockets \
		--enable-zip \
		--with-bz2 \
		--with-curl \
		--with-fpm-group=www-data \
		--with-fpm-user=www-data \
		--with-gd \
		--with-gettext \
		--with-openssl \
		--with-pcre-regex \
		--with-pdo-mysql \
		--with-pdo-pgsql \
		--with-readline \
		--with-xsl \
		--with-zlib && \

	cd /tmp/build/php/php-${PHP_VERSION} && \
	# Compile, test and install
	make -j$(nproc) build && \
	make install && \

	# Compile Xdebug
	mkdir -p /tmp/build/xdebug && \
	cd /tmp/build/xdebug && \
	curl -SLO \
		"https://github.com/xdebug/xdebug/archive/XDEBUG_"$(echo ${XDEBUG_VERSION} | sed "s/\./_/g")".tar.gz" && \
	tar -xvzf "XDEBUG_"$(echo ${XDEBUG_VERSION} | sed "s/\./_/g")".tar.gz" && \
	cd "xdebug-XDEBUG_"$(echo ${XDEBUG_VERSION} | sed "s/\./_/g") && \
	phpize && \
	./configure && \
	make && \
	make install && \

	# Fix permissions
	chown -R www-data:www-data /usr/local/nginx/html && \

	# Symlink Nginx binary
	ln -s /usr/local/nginx/sbin/nginx /usr/local/sbin/ && \

	# Copy PHP-FPM configuration files
	cp /tmp/build/php/php-${PHP_VERSION}/sapi/fpm/php-fpm.conf /usr/local/etc/php-fpm.conf && \
	cp /tmp/build/php/php-${PHP_VERSION}/sapi/fpm/www.conf /usr/local/etc/www.conf && \
	cp /tmp/build/php/php-${PHP_VERSION}/php.ini-development /usr/local/php/php.ini && \

	# Patch PHP-FPM for proper loading www.conf
	sed -Ei \
		-e 's/^;?\s*daemonize\s*=\s*yes/daemonize = no/' \
		-e 's/^;?\s*include=NONE\/etc\/php-fpm.d\/\*.conf/include=\/usr\/local\/etc\/www.conf/' \
		/usr/local/etc/php-fpm.conf && \

	# Patch www.conf config connection establishment
	sed -Ei \
		-e 's/^;?\s*listen\s*=.*/listen = \/var\/run\/php-fpm.sock/' \
		-e 's/^;?\s*?\s*listen.owner\s*=.*/listen.owner = www-data/' \
		-e 's/^;?\s*?\s*listen.group\s*=.*/listen.group = www-data/' \
		-e 's/^;?\s*?\s*listen.mode\s*=.*/listen.mode = 0660/' \
		/usr/local/etc/www.conf && \

	# Patch PHP config files on the fly
	sed -Ei \
		-e 's/^;?\s*expose_php\s*=.*/expose_php = Off/' \
		-e 's/^;?\s*cgi.fix_pathinfo\s*=.*/cgi.fix_pathinfo=0/' \
		-e 's/^;?\s*error_log\s*=.*/error_log = \/usr\/local\/nginx\/logs\/error-php.log/' \
		-e 's/^;?\s*date.timezone\s*=.*/date.timezone = \"UTC\"/' \
		-e 's/^;?\s*opcache.enable\s*=.*/opcache.enable = 1/' \
		-e 's/^;?\s*opcache.enable_cli\s*=.*/opcache.enable_cli=1/' \
		-e 's/^;?\s*opcache.memory_consumption\s*=.*/opcache.memory_consumption = 256/' \
		-e 's/^;?\s*opcache.max_accelerated_files\s=.*/opcache.max_accelerated_files = 10000/' \
		/usr/local/php/php.ini && \

	# Install PHP composer
	php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \
	php -r "if (hash_file('SHA384', 'composer-setup.php') === trim(file_get_contents('https://composer.github.io/installer.sig'))) { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;" && \
	php composer-setup.php --install-dir=/usr/local/bin --filename=composer && \
	php -r "unlink('composer-setup.php');" && \

	# Configure Honcho
	mv /tmp/build/scripts/Procfile / && \

	# Add entrypoint for docker
	mv /tmp/build/scripts/docker-entrypoint / && \
	chmod +x /docker-entrypoint && \
	mv /tmp/build/scripts/fix-permission / && \
	chmod +x /fix-permission && \

	# Final cleanup
	apt-get remove -y \
		autoconf \
		bison \
		build-essential \
		curl \
		pkg-config \
		python-pip \
		re2c && \

	apt-get autoremove -y && \

	rm -rf /var/lib/apt/lists/* && \
	rm -rf /tmp/build

# Declare entrypoint
ENTRYPOINT ["/docker-entrypoint"]

# Define default command
CMD ["server"]

# Define Workdir
WORKDIR "/usr/local/nginx/html"

# Exposing ports
EXPOSE 80/tcp 443/tcp
