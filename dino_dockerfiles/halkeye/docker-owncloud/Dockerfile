FROM php:7.1-apache
MAINTAINER Gavin Mogan "gavin@gavinmogan.com"
ENV OWNCLOUD_VERSION=10.0.0 OWNCLOUD_ROOT=/var/www/owncloud

RUN apt-get -y update && apt-get install -y \
      bzip2 \
      libcurl4-openssl-dev \
      libfreetype6-dev \
      libicu-dev \
      libjpeg-dev \
      libmcrypt-dev \
      libmemcached-dev \
      libpng12-dev \
      libpq-dev \
      libxml2-dev \
      build-essential \
      apache2-threaded-dev \
      && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

#gpg key from https://owncloud.org/owncloud.asc
RUN gpg --keyserver ha.pool.sks-keyservers.net --recv-keys E3036906AD9F30807351FAC32D5D5E97F6978A26

# https://doc.owncloud.org/server/8.1/admin_manual/installation/source_installation.html#prerequisites
RUN docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \
  && docker-php-ext-install gd intl mbstring mcrypt opcache pdo_mysql zip
#  && pecl install rar && docker-php-ext-enable rar


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

# PECL extensions
RUN pecl install APCu-5.1.8 redis memcached \
  && docker-php-ext-enable apcu redis memcached

RUN mkdir -p /root/src/mod_rpaf \
    && curl -L https://github.com/gnif/mod_rpaf/archive/stable.tar.gz | tar xz --strip-components=1 -C /root/src/mod_rpaf \
    && (cd /root/src/mod_rpaf && make && make install)

RUN a2enmod rewrite

RUN { \
    echo 'LoadModule              rpaf_module /usr/lib/apache2/modules/mod_rpaf.so'; \
    echo 'RPAF_Enable             On'; \
    echo 'RPAF_ProxyIPs           172.17.0.1 127.0.0.1 10.0.0.0/24'; \
    echo 'RPAF_SetHostName        On'; \
    echo 'RPAF_SetHTTPS           On'; \
    echo 'RPAF_SetPort            On'; \
    echo 'RPAF_ForbidIfNotProxy   On'; \
  } > /etc/apache2/mods-enabled/rpaf.conf

# Create config && data Directory
RUN mkdir ${OWNCLOUD_ROOT} ${OWNCLOUD_ROOT}/data ${OWNCLOUD_ROOT}/config \
    && rm -rf /var/www/html && ln -s ${OWNCLOUD_ROOT} /var/www/html

RUN curl -fsSL -o owncloud.tar.bz2 \
    "https://download.owncloud.org/community/owncloud-${OWNCLOUD_VERSION}.tar.bz2" \
  && curl -fsSL -o owncloud.tar.bz2.asc \
    "https://download.owncloud.org/community/owncloud-${OWNCLOUD_VERSION}.tar.bz2.asc" \
  && gpg --verify owncloud.tar.bz2.asc \
  && tar --strip-components=1 -xjf owncloud.tar.bz2 -C ${OWNCLOUD_ROOT} \
  && rm owncloud.tar.bz2 owncloud.tar.bz2.asc

# Install all the plugins
RUN mkdir -p ${OWNCLOUD_ROOT}/apps/notes \
    && curl -L https://github.com/owncloud/notes/archive/v2.0.tar.gz | tar xz --strip-components=1 -C ${OWNCLOUD_ROOT}/apps/notes
RUN mkdir -p ${OWNCLOUD_ROOT}/apps/ownnote \
    && curl -L https://github.com/Fmstrat/ownnote/archive/ownNote-1.05.tar.gz | tar xz --strip-components=1 -C ${OWNCLOUD_ROOT}/apps/ownnote
#RUN mkdir -p ${OWNCLOUD_ROOT}/apps/ocsms \
#    && curl -L https://github.com/nerzhul/ocsms/archive/v1.5.0.tar.gz | tar xz --strip-components=1 -C ${OWNCLOUD_ROOT}/apps/ocsms
RUN mkdir -p ${OWNCLOUD_ROOT}/apps/qownnotesapi \
    && curl -L https://apps.owncloud.com/CONTENT/content-files/173817-qownnotesapi.tar.gz | tar xz --strip-components=1 -C ${OWNCLOUD_ROOT}/apps/qownnotesapi
# Temp
RUN apt-get -y update && apt-get install -y patch && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN mkdir -p ${OWNCLOUD_ROOT}/apps/contacts \
    && curl -L https://github.com/owncloud/contacts/archive/1.5.2.tar.gz | tar xz --strip-components=1 -C ${OWNCLOUD_ROOT}/apps/contacts
RUN mkdir -p ${OWNCLOUD_ROOT}/apps/tasks \
    && curl -L https://github.com/owncloud/tasks/archive/v0.9.4.tar.gz | tar xz --strip-components=1 -C ${OWNCLOUD_ROOT}/apps/tasks
RUN mkdir -p ${OWNCLOUD_ROOT}/apps/calendar \
    && curl -L https://github.com/owncloud/calendar/archive/v1.3.3.tar.gz | tar xz --strip-components=1 -C ${OWNCLOUD_ROOT}/apps/calendar
RUN mkdir -p ${OWNCLOUD_ROOT}/apps/files_opds \
    && curl -L https://github.com/Yetangitu/owncloud-apps/raw/master/dist/files_opds-0.8.2.tar.gz | tar xz --strip-components=1 -C ${OWNCLOUD_ROOT}/apps/files_opds
# Move app - https://apps.owncloud.com/content/show.php?content=150271
#RUN curl -L https://apps.owncloud.com/CONTENT/content-files/150271-files_mv.tar.gz | tar xz -C ${OWNCLOUD_ROOT}/apps
# Mozilla Sync - https://apps.owncloud.com/content/show.php/Mozilla+Sync?content=161793
#RUN mkdir -p ${OWNCLOUD_ROOT}/apps/mozilla_sync \
#    && curl -L https://github.com/owncloud/mozilla_sync/archive/v1.4.tar.gz | tar xz --strip-components=1 -C ${OWNCLOUD_ROOT}/apps/mozilla_sync
#RUN mkdir -p ${OWNCLOUD_ROOT}/apps/files_epubviewer \
#    && curl -L https://apps.owncloud.com/CONTENT/content-files/166614-files_epubviewer_oc7.tar.gz | tar xz --strip-components=1 -C ${OWNCLOUD_ROOT}/apps/files_epubviewer

# lock down ownership of everything
RUN chown -R www-data:www-data ${OWNCLOUD_ROOT}

VOLUME ["${OWNCLOUD_ROOT}/data", "${OWNCLOUD_ROOT}/config", "/tmp/mysql.sock", "/var/run/mysqld/mysqld.sock"]
EXPOSE 80

CMD ["apache2-foreground"]
