FROM php:7.0-fpm

MAINTAINER Dan Braghis <dan@zerolab.org>

ENV NGINX_VERSION 1.12.0-1~jessie
ENV NJS_VERSION   1.12.0.0.1.10-1~jessie

RUN apt-get update \
  && apt-get install --no-install-recommends --no-install-suggests -y gnupg-curl \
  && \
  NGINX_GPGKEY=573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62; \
  found=''; \
  for server in \
    ha.pool.sks-keyservers.net \
    hkp://keyserver.ubuntu.com:80 \
    hkp://p80.pool.sks-keyservers.net:80 \
    pgp.mit.edu \
  ; do \
    echo "Fetching GPG key $NGINX_GPGKEY from $server"; \
    apt-key adv --keyserver "$server" --keyserver-options timeout=10 --recv-keys "$NGINX_GPGKEY" && found=yes && break; \
  done; \
  test -z "$found" && echo >&2 "error: failed to fetch GPG key $NGINX_GPGKEY" && exit 1; \
  apt-get remove --purge -y gnupg-curl && apt-get -y --purge autoremove && rm -rf /var/lib/apt/lists/* \
  && echo "deb http://nginx.org/packages/debian/ jessie nginx" >> /etc/apt/sources.list \
  && apt-get update \
  && apt-get install --no-install-recommends --no-install-suggests -y \
            nginx=${NGINX_VERSION} \
            nginx-module-xslt=${NGINX_VERSION} \
            nginx-module-geoip=${NGINX_VERSION} \
            nginx-module-image-filter=${NGINX_VERSION} \
            nginx-module-njs=${NJS_VERSION} \
            gettext-base \
  && rm -rf /var/lib/apt/lists/*

# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
  && ln -sf /dev/stderr /var/log/nginx/error.log

WORKDIR /var/www/html
VOLUME /var/www/html

COPY config/nginx.conf /etc/nginx/nginx.conf
COPY config/drupal8.conf /etc/nginx/conf.d/default.conf

ENV NGINX_SERVER_NAME="_"
ENV NGINX_DOCROOT="/var/www/html"

RUN sed -i 's@%NGINX_SERVER_NAME%@'"${NGINX_SERVER_NAME}"'@' /etc/nginx/conf.d/*.conf
RUN sed -i 's@%NGINX_DOCROOT%@'"${NGINX_DOCROOT}"'@' /etc/nginx/conf.d/*.conf

STOPSIGNAL SIGQUIT

RUN apt-get update -y && apt-get -y install git curl unzip mariadb-client-10.0 \
    libjpeg62-turbo-dev libpng12-dev libpq-dev \
    libcurl4-openssl-dev libfreetype6-dev libxslt1-dev libxml2-dev \
    && docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \
    && docker-php-ext-install dom gd hash json mbstring pdo_mysql zip xml \
    # Cleanup
    && DEBIAN_FRONTEND=noninteractive apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN curl -L https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
RUN export PATH="$HOME/.composer/vendor/bin:$PATH"

EXPOSE 80 9000

CMD nginx -g daemon off; php-fpm
