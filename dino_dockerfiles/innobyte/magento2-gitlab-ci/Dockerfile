FROM php:7.0
MAINTAINER Alin Alexandru <alin.alexandru@innobyte.com>

RUN apt-get update \
   && apt-get install -y \
      git-core \
      pigz unzip zip \
   && docker-php-ext-install mbstring \
   && docker-php-ext-install pdo_mysql \
   && apt-get install -y libxml2-dev \
       && docker-php-ext-install soap \
   && apt-get install -y libmcrypt4 libmcrypt-dev \
       && docker-php-ext-install mcrypt \
   && apt-get install -y libxslt-dev \
       && docker-php-ext-install xsl \
   && apt-get install -y libicu-dev \
       && docker-php-ext-install intl \
   && apt-get install -y libpng-dev libjpeg-dev \
       && docker-php-ext-configure gd --with-jpeg-dir=/usr/lib \
       && docker-php-ext-install gd \
   && apt-get install -y zlib1g-dev \
       && docker-php-ext-install zip \
   && docker-php-ext-install bcmath \
   && rm -rf /var/lib/apt/lists/*

# PHP Configuration
RUN echo "memory_limit=-1" > $PHP_INI_DIR/conf.d/memory-limit.ini
RUN echo "date.timezone=UTC" > $PHP_INI_DIR/conf.d/date_timezone.ini

# Install composer and put binary into $PATH
RUN curl -sS https://getcomposer.org/installer | php \
    && mv composer.phar /usr/local/bin/ \
    && ln -s /usr/local/bin/composer.phar /usr/local/bin/composer

# Install phpunit and put binary into $PATH
RUN curl -sSLo phpunit.phar https://phar.phpunit.de/phpunit-6.phar \
    && chmod 755 phpunit.phar \
    && mv phpunit.phar /usr/local/bin/ \
    && ln -s /usr/local/bin/phpunit.phar /usr/local/bin/phpunit

# Install PHP Code sniffer
RUN curl -OL https://squizlabs.github.io/PHP_CodeSniffer/phpcs.phar \
    && chmod 755 phpcs.phar \
    && mv phpcs.phar /usr/local/bin/ \
    && ln -s /usr/local/bin/phpcs.phar /usr/local/bin/phpcs \
    && curl -OL https://squizlabs.github.io/PHP_CodeSniffer/phpcbf.phar \
    && chmod 755 phpcbf.phar \
    && mv phpcbf.phar /usr/local/bin/ \
    && ln -s /usr/local/bin/phpcbf.phar /usr/local/bin/phpcbf
    
# Install deployer
RUN curl -LO https://deployer.org/deployer.phar \
    && mv deployer.phar /usr/local/bin/dep \
    && chmod +x /usr/local/bin/dep
