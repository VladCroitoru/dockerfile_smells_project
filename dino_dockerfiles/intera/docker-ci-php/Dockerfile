FROM ubuntu:20.04

COPY install_composer.sh /tmp/install_composer.sh

ENV DEBIAN_FRONTEND noninteractive
ENV LANG C.UTF-8

RUN apt-get update \
	&& apt-get dist-upgrade -y \
	&& apt-get install -y software-properties-common \
	&& add-apt-repository ppa:ondrej/php \
	&& apt-get update -y

RUN apt-get install -y \
		php8.0-apcu \
		php8.0-cli \
		php8.0-curl \
		php8.0-gd \
		php8.0-imap \
		php8.0-intl \
		php8.0-ldap \
		php8.0-mbstring \
		php8.0-mysql \
		php8.0-pgsql \
		php8.0-soap \
		php8.0-sqlite3 \
		php8.0-xdebug \
		php8.0-phpdbg \
		php8.0-xml \
		php8.0-zip

RUN apt-get install -y \
		imagemagick \
		language-pack-de \
		wget \
		git \
		zip \
		unzip \
		openssh-client \
		mysql-client \
		rsync \
		curl \
		apt-transport-https \
		lsb-release \
		gnupg \
		parallel

RUN bash /tmp/install_composer.sh \
	&& mv composer.phar /usr/local/bin/

RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
    && echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list \
    && curl -sL https://deb.nodesource.com/setup_14.x | bash -

RUN apt-get install -y nodejs yarn

RUN apt-get purge -y software-properties-common apt-transport-https lsb-release gnupg \
    && apt-get --purge -y autoremove \
	&& apt-get autoclean \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/*

# Disable xdebug by default to improve build performance!
RUN phpdismod xdebug
