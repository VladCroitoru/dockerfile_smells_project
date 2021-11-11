FROM php:5.4-apache
# Install modules
RUN apt-get update && apt-get install -y \
    wget\
    git\
    zlib1g-dev \
    php-pear \

    libfreetype6-dev \
    libjpeg62-turbo-dev \
    libmcrypt-dev \
    libpng12-dev \
    build-essential \
    chrpath \

   libssl-dev\
   libxft-dev\
   libfreetype6 \
   libfreetype6-dev\
   libfontconfig1 \

    libfontconfig1-dev\
    && docker-php-ext-install iconv mcrypt \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install gd \
    && docker-php-ext-install mbstring\
    && docker-php-ext-install zip

RUN curl -s https://getcomposer.org/installer | php
RUN mv composer.phar /usr/local/bin/composer


RUN wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-1.9.8-linux-x86_64.tar.bz2
RUN tar xvjf phantomjs-1.9.8-linux-x86_64.tar.bz2

RUN mv phantomjs-1.9.8-linux-x86_64 /usr/local/share
RUN ln -sf /usr/local/share/phantomjs-1.9.8-linux-x86_64/bin/phantomjs /usr/local/bin

WORKDIR /home/behat


