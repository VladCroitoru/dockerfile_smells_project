FROM    php:7.1-apache
RUN     apt-get update && apt-get install -y \
        libbz2-dev \
        libcurl3-dev \
        libedit-dev \
	libfreetype6-dev \
        libjpeg62-turbo-dev \
	libldap2-dev \
        libmcrypt-dev \
        libpng12-dev \
        libpq-dev \
        libxml2-dev \
	libxslt-dev \
	ssmtp \
	&& ln -fs /usr/lib/x86_64-linux-gnu/libldap.so /usr/lib/ \
	&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
	&& docker-php-ext-install \
		mysqli \
		curl \
		gd \
		mcrypt \
		readline \
		ftp \
		iconv \
		json \
		mbstring \
		soap \
		xml \
		xmlrpc \
		xmlwriter \
		zip \
		xsl \
		bz2 \
		ldap \
	&& CFLAGS="-I/usr/src/php" docker-php-ext-install xmlreader \
#	&& apt-get purge -y --auto-remove \
#		libbz2-dev \
#		libcurl3-dev \
#		libedit-dev \
#		libfreetype6-dev \
#		libjpeg62-turbo-dev \
#		libldap2-dev \
#		libmcrypt-dev \
#		libpng12-dev \
#		libpq-dev \
#		libxml2-dev \
#		libxslt-dev \
	&& rm -r /var/lib/apt/lists/*
