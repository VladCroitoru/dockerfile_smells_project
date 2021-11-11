FROM richarvey/nginx-php-fpm:1.2.2
MAINTAINER Women's Tennis Association <admin@wtanetworks.com>

# install the PHP extensions we need
RUN apk upgrade --update && \
    apk add \
         autoconf \
         g++ \
         make \
         libpng-dev \
         libjpeg-turbo-dev \
         postgresql-dev \
         libmcrypt-dev \
         openldap-dev \
         ldb-dev \
         icu-dev \
         gmp-dev \
         imagemagick-dev \
         pcre-dev \
         libtool \
         openssh \
         mysql-client \
         git \
    && echo "root:Docker!" | chpasswd \
    && pecl install imagick-beta \
    && yes '' | pecl install -f redis \
    && docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \
    && docker-php-ext-install gd \
         json \
         mysqli \
         opcache \
         pdo \
         pdo_mysql \
         pdo_pgsql \
         pgsql \
         ldap \
         intl \
         mcrypt \
         gmp \
         zip \
         bcmath \
         mbstring \
         pcntl \
         ftp \
    && docker-php-ext-enable imagick redis


COPY init_container.sh /bin/
COPY hostingstart.html /home/site/wwwroot/hostingstart.html

RUN \
   mkdir -p /home/LogFiles \
   && rm -rf /var/www/html \
   && ln -s /home/site/wwwroot /var/www/html \
   && chmod 755 /bin/init_container.sh

RUN { \
                echo 'opcache.memory_consumption=128'; \
                echo 'opcache.interned_strings_buffer=8'; \
                echo 'opcache.max_accelerated_files=4000'; \
                echo 'opcache.revalidate_freq=60'; \
                echo 'opcache.fast_shutdown=1'; \
                echo 'opcache.enable_cli=1'; \
    } > /usr/local/etc/php/conf.d/opcache-recommended.ini

RUN { \
                echo 'error_log=/var/log/apache2/php-error.log'; \
                echo 'display_errors=Off'; \
                echo 'log_errors=On'; \
                echo 'display_startup_errors=Off'; \
                echo 'date.timezone=UTC'; \
    } > /usr/local/etc/php/conf.d/php.ini

COPY sshd_config /etc/ssh/

EXPOSE 2222 8080

ENV PORT 8080
ENV WEBSITE_ROLE_INSTANCE_ID localRoleInstance
ENV WEBSITE_INSTANCE_ID localInstance


#Composer
ENV COMPOSER_ALLOW_SUPERUSER 1
ENV COMPOSER_HOME /home/.composer
ENV COMPOSER_VERSION "1.4.2"
ENV COMPOSER_SETUP_SHA 669656bab3166a7aff8a7506b8cb2d1c292f042046c5a994c43155c0be6190fa0355160742ab2e1c88d40d5be660b410
ENV PATH ${PATH}:/usr/local/php/bin

# Install Composer
RUN php -r "readfile('https://getcomposer.org/installer');" > /tmp/composer-setup.php \
    && php -r "if (hash('SHA384', file_get_contents('/tmp/composer-setup.php')) === getenv('COMPOSER_SETUP_SHA')) { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('/tmp/composer-setup.php'); echo PHP_EOL; exit(1); } echo PHP_EOL;" \
    && mkdir -p /composer/bin \
    && php /tmp/composer-setup.php --install-dir=/usr/local/bin/ --filename=composer --version=${COMPOSER_VERSION} \
    && rm /tmp/composer-setup.php

#Drush
RUN php -r "readfile('http://files.drush.org/drush.phar');" > /usr/local/bin/drush \
    && chmod +x /usr/local/bin/drush

WORKDIR /var/www/html

ENTRYPOINT ["/bin/init_container.sh"]
