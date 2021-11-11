FROM php:5.6-apache

RUN a2enmod rewrite expires

# install the PHP extensions we need
RUN apt-get -qqy update && apt-get install -qqy \
  libpng12-dev libjpeg-dev libmcrypt-dev libxml2-dev libxslt-dev \
  cron logrotate \
  && rm -rf /var/lib/apt/lists/* \
  && docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \
  && docker-php-ext-install gd \
    mysqli mysql opcache mcrypt soap xsl zip

# set recommended PHP.ini settings
# see https://secure.php.net/manual/en/opcache.installation.php
RUN { \
  echo 'opcache.memory_consumption=128'; \
  echo 'opcache.interned_strings_buffer=8'; \
  echo 'opcache.max_accelerated_files=4000'; \
  echo 'opcache.revalidate_freq=60'; \
  echo 'opcache.fast_shutdown=1'; \
  echo 'opcache.enable_cli=1'; \
} > /usr/local/etc/php/conf.d/opcache-recommended.ini

# enable mod_rewrite
RUN a2enmod rewrite

WORKDIR /var/www/html

# can be overridden/set in compose file
ENV OJS_VERSION 3.0.2

# upstream tarballs include ./ojs-${OJS_VERSION}/ so this gives us /var/www/ojs
RUN curl -o ojs.tar.gz -SL http://pkp.sfu.ca/ojs/download/ojs-${OJS_VERSION}.tar.gz \
  && tar -xzf ojs.tar.gz -C /var/www \
  && rm ojs.tar.gz \
    && mv /var/www/ojs-${OJS_VERSION} /var/www/ojs \
  && chown -R www-data:www-data /var/www/ojs

COPY PKPRequest.inc.php /var/www/ojs/lib/pkp/classes/core/PKPRequest.inc.php

# creating a directory to save uploaded files.
RUN mkdir /var/www/files \
  && chown -R www-data:www-data /var/www/files

# environment to set database params
ENV OJS_DB_HOST localhost
ENV OJS_DB_USER ojs
ENV OJS_DB_PASSWORD ojs
ENV OJS_DB_NAME ojs

# Site servername
ENV SERVERNAME ojs-v3.scielo.org
ENV APACHE_LOG_DIR /var/log/apache2
ENV LOG_NAME 0js-v3_scielo_org

# Add crontab running runSheduledTasks.php
COPY ojs-crontab.conf /ojs-crontab.conf
RUN sed -i 's:INSTALL_DIR:'`pwd`':' /ojs-crontab.conf \
  && sed -i 's:FILES_DIR:/var/www/ojs/files:' /ojs-crontab.conf \
  && echo "$(cat /ojs-crontab.conf)" \
  # Use the crontab file
  && crontab /ojs-crontab.conf \
  && touch /var/log/cron.log

COPY 000-default.conf /etc/apache2/sites-enabled/000-default.conf

EXPOSE 80

# Add startup script to the container.
COPY ojs-startup.sh /ojs-startup.sh

# Execute the containers startup script which will start many processes/services
CMD ["/bin/bash", "/ojs-startup.sh"]
