FROM php:5.5-apache

# General purpose packages.
RUN apt-get update && apt-get -y install git-core wget mysql-client php5-mysql ant openjdk-7-jdk \
       	libfreetype6-dev \
   		libjpeg62-turbo-dev \
        libmcrypt-dev \
        libpng12-dev \
    && docker-php-ext-install iconv mcrypt \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install gd \
    && docker-php-ext-install mbstring \
    && docker-php-ext-install pdo pdo_mysql

# enable mod_rewrite
RUN a2enmod rewrite

# drush: instead of installing a package, pull via composer into /opt/composer
# http://www.whaaat.com/installing-drush-7-using-composer
RUN curl -sS https://getcomposer.org/installer | php && \
    mv composer.phar /usr/local/bin/composer && \
    COMPOSER_HOME=/opt/composer composer --quiet global require drush/drush:dev-master && \
    ln -s /opt/composer/vendor/drush/drush/drush /bin/drush

# Add drush comand https://www.drupal.org/project/registry_rebuild
RUN wget http://ftp.drupal.org/files/projects/registry_rebuild-7.x-2.2.tar.gz && \
    tar xzf registry_rebuild-7.x-2.2.tar.gz && \
    rm registry_rebuild-7.x-2.2.tar.gz && \
    mv registry_rebuild /opt/composer/vendor/drush/drush/commands

# Check drush.
RUN /bin/drush --version

ENV SSH_KEY id_rsa

RUN  echo "IdentityFile ~/.ssh/$SSH_KEY" >> /etc/ssh/ssh_config

VOLUME ["/var/www/html"]

EXPOSE 80