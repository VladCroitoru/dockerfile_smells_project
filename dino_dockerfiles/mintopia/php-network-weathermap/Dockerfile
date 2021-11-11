FROM php:5-cli
MAINTAINER Jessica Smith <jess@mintopia.net>

WORKDIR /tmp

RUN \
  apt-get update && \
  apt-get install -y \
	wget \
	libfreetype6-dev \
        libjpeg62-turbo-dev \
	rrdtool \
        libpng-dev && \
  docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ && \
  docker-php-ext-install -j$(nproc) gd && \
  wget https://github.com/howardjones/network-weathermap/archive/version-0.98.tar.gz && \
  tar zxvf version-0.98.tar.gz && \
  rm -f version-0.98.tar.gz && \
  mv network-weathermap-version-0.98 /opt/network-weathermap && \
  chmod +x /opt/network-weathermap/weathermap && \
  mkdir /config && \
  mkdir /output && \
  rm -rf /var/lib/apt/lists/* && \
  php /opt/network-weathermap/check.php
  
COPY weathermap.php /opt/weathermap.php
VOLUME /config /output

WORKDIR /opt/network-weathermap
CMD ["php", "/opt/weathermap.php"]
