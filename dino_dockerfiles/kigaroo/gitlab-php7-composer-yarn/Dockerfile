FROM php:7.1.8

ENV PHANTOM_JS "phantomjs-2.1.1-linux-x86_64"

RUN set -x \
 && apt-get update -y \
 && apt-get install -y wget apt-transport-https \
 && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
 && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google.list \
 && curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
 && echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list \
 && curl -sL https://deb.nodesource.com/setup_8.x | bash - \
 && apt-get update -y \
 && apt-get install -y git zip libmcrypt-dev libcurl4-gnutls-dev libicu-dev \
                       libfreetype6-dev libjpeg-dev libpng-dev libxml2-dev \
                       libbz2-dev libc-client-dev libkrb5-dev  mysql-client \ 
                       nodejs yarn google-chrome-stable \
 && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/  \
 && docker-php-ext-configure imap --with-kerberos --with-imap-ssl \
 && docker-php-ext-install mbstring mcrypt curl json intl gd xml zip bz2 opcache pdo_mysql pcntl imap exif bcmath \
 && pecl install xdebug \
 && echo "date.timezone = Europe/Berlin" > /usr/local/etc/php/conf.d/timezone.ini \
 && echo "memory_limit = -1" > /usr/local/etc/php/conf.d/memory.ini  \
 && wget -O /usr/local/bin/composer https://getcomposer.org/download/1.7.2/composer.phar \
 && chmod +x /usr/local/bin/composer \
 && wget https://chromedriver.storage.googleapis.com/2.42/chromedriver_linux64.zip -O /tmp/chromedriver.zip \
 && unzip /tmp/chromedriver.zip -d /usr/local/bin \
 && wget https://github.com/Medium/phantomjs/releases/download/v2.1.1/$PHANTOM_JS.tar.bz2 -O /tmp/$PHANTOM_JS.tar.bz2 \
 && tar xvjf /tmp/$PHANTOM_JS.tar.bz2 -C /usr/local/bin --strip-components 2 $PHANTOM_JS/bin/phantomjs \
 && apt-get autoclean -y \
 && apt-get --purge autoremove -y \
 && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \ 
 && php -i

