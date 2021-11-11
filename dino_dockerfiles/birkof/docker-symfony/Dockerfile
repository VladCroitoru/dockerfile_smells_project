# Import base image
FROM birkof/ubuntu

# PHP7.0 & Java repo & Blackfire.io && latest Node.js package
RUN export LANG=C.UTF-8 \
    && add-apt-repository -y ppa:ondrej/php \
    && wget -O - https://packagecloud.io/gpg.key | sudo apt-key add - \
    && echo "deb http://packages.blackfire.io/debian any main" | sudo tee /etc/apt/sources.list.d/blackfire.list \
    && curl -sL https://deb.nodesource.com/setup_6.x | bash - \
    && apt-get install -yq --no-install-recommends nodejs

# Install nginx & php7-fpm package and some dependecies
RUN apt-get install -yq --no-install-recommends \
    nginx \
    php7.0 \
    php7.0-dev \
    php7.0-fpm \
    php7.0-mysql \
    php7.0-mcrypt \
    php7.0-mbstring \
    php7.0-bcmath \
    php7.0-soap \
    php7.0-json \
    php7.0-xml \
    php7.0-xmlrpc \
    php7.0-zip \
    php7.0-gd \
    php7.0-curl \
    php7.0-ldap \
    php7.0-intl \
    php7.0-opcache \
    php-xdebug \
    php-redis \
    php-apcu \
    php-memcache \
    php-memcached \
    php-pear \
    blackfire-php

# Injecting container assets files
ADD .docker /

# Set timezone in php.ini
RUN sed -i".bak" "s@^;date.timezone =.*@date.timezone = $TIMEZONE@" /etc/php/7.0/*/php.ini

# Tweak php-fpm logging
RUN mkdir -p /var/log/php7 \
    && sed -i 's/;log_level = .*/log_level = debug/g' /etc/php/7.0/fpm/php-fpm.conf \
    && sed -i 's/;daemonize = yes/daemonize = no/g' /etc/php/7.0/fpm/php-fpm.conf \
    && sed -i -e "s/^\error_log = .*$/error_log = \/var\/log\/php7\/php-fpm.log/g" /etc/php/7.0/fpm/php-fpm.conf

# Activate CLI extensions
RUN find /etc/php/7.0/cli/conf.d/ -name "*.ini" -exec sed -i -re 's/^(\s*)#(.*)/\1;\2/g' {} \;

# Change the UID of www-data for OSX writing permission problem
RUN usermod -u 1000 www-data

# Install composer
RUN curl -LsS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer \
    && composer --version

# get PHP CodeSniffer (https://pear.php.net/package/PHP_CodeSniffer)
RUN curl -LsS https://squizlabs.github.io/PHP_CodeSniffer/phpcs.phar -o /usr/local/bin/phpcs \
    && chmod a+x /usr/local/bin/phpcs \
    && phpcs --version

# php-cs-fixer
RUN curl http://get.sensiolabs.org/php-cs-fixer.phar -o php-cs-fixer \
    && chmod a+x php-cs-fixer \
    && mv php-cs-fixer /usr/local/bin/php-cs-fixer

# Install phpunit
RUN curl -LsS https://phar.phpunit.de/phpunit.phar -o /usr/local/bin/phpunit \
    && chmod a+x /usr/local/bin/phpunit \
    && phpunit --version

# Install Symfony Installer
RUN curl -LsS http://symfony.com/installer -o /usr/local/bin/symfony \
    && chmod a+x /usr/local/bin/symfony \
    && symfony --version

# Symfony console shortcuts
RUN echo '#!/bin/bash' > /usr/local/bin/dev && echo 'php /var/www/symfony/bin/console --env=dev $@' >> /usr/local/bin/dev && chmod +x /usr/local/bin/dev \
    && echo '#!/bin/bash' > /usr/local/bin/prod && echo 'php /var/www/symfony/bin/console --env=prod $@' >> /usr/local/bin/prod && chmod +x /usr/local/bin/prod

# Clean up the mess
RUN apt-get autoclean \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Exposed port/s
EXPOSE 22 80

# Working dir
WORKDIR /var/www
