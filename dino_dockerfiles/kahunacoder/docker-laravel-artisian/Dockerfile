FROM php:5.6-cli

MAINTAINER "Gary Smith" <docker@kc.gs>

WORKDIR /tmp

RUN apt-get update -y && \
    apt-get install -y \
    libjpeg62-turbo-dev \
    libmcrypt-dev \
    libpng12-dev \
	libcurl4-gnutls-dev \
	libxml2-dev \
	libbz2-dev \
	re2c \
	libpng++-dev \
    libpng3 \
    libjpeg-dev \
    libvpx-dev \
    zlib1g-dev \
    libgd-dev \
    sqlite3 \
    libsqlite3-dev \

    && docker-php-ext-install pdo \
    && docker-php-ext-install pdo_mysql \
    && docker-php-ext-install pdo_sqlite \
    && docker-php-ext-install gd \
	&& docker-php-ext-install mcrypt

VOLUME ["/app"]
WORKDIR /app

ENTRYPOINT ["php", "artisan"]
#CMD ["--help"]