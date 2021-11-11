FROM php:7.0-apache
LABEL maintainer="jarlave <jarlave@pm.me>"

RUN apt-get update && apt-get install -y \
      imagemagick \
      libav-tools \
      libfreetype6-dev \
      libjpeg62-turbo-dev \
      libpng-dev \
      patch \
      unzip \
      zip \
      && rm -rf /usr/share/doc/* && \
      rm -rf /usr/share/info/* && \
      rm -rf /tmp/* && \
      rm -rf /var/tmp/* && \
      docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ && \
      docker-php-ext-install gd && \
      docker-php-ext-install exif

ENV H5AI_VERSION 0.29.2
ENV PREFIX=""

RUN curl -L https://release.larsjung.de/h5ai/h5ai-${H5AI_VERSION}.zip > /usr/src/h5ai-${H5AI_VERSION}.zip && \
    unzip /usr/src/h5ai-${H5AI_VERSION}.zip && \
    rm -f /usr/src/h5ai-${H5AI_VERSION}.zip
COPY class-setup.patch /usr/src/class-setup.patch
# patch to add prefix tobe used in reverse proxy
RUN patch -p1 /var/www/html/_h5ai/private/php/core/class-setup.php /usr/src/class-setup.patch
COPY h5ai.conf /etc/apache2/conf-enabled/h5ai.conf
COPY options.json /var/www/html/_h5ai/private/conf/options.json
RUN chown www-data:www-data /var/www/html/_h5ai/private/cache
RUN chown www-data:www-data /var/www/html/_h5ai/public/cache
