FROM php:7.2.3-cli

# Install PHP and NPM dependencies
RUN apt-get update && \
    apt-get install -y libsqlite3-dev libfreetype6 libfontconfig1 gnupg2 git unzip bzip2 make g++

RUN docker-php-ext-install -j$(nproc) pdo_sqlite pdo_mysql && \
    pecl install -f xdebug && \
    docker-php-ext-enable xdebug

# Install Composer
RUN curl -sS https://getcomposer.org/installer | php && \
    mv composer.phar /usr/bin/composer

# Install NodeJS
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - && \
    apt-get install nodejs -y

# NPM Install
RUN npm install -g bower --unsafe-perm && \
    npm install --global gulp --unsafe-perm && \
    npm install -g karma --unsafe-perm

# Fix PHP.ini
RUN echo 'memory_limit=2048M\n\
date.timezone=Europe/Paris\n'\
>> /usr/local/etc/php/php.ini

RUN useradd -r -u 1040 creativedata --create-home

RUN mkdir /workspace
WORKDIR /workspace

ADD build.sh /build.sh
RUN chmod 755 /build.sh

USER creativedata
CMD ["/build.sh"]
