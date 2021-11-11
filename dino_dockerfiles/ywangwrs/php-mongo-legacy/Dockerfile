#FROM php:5-apache
#FROM php:5.6.12-apache
FROM php:5.6.31-apache

RUN echo "deb [check-valid-until=no] http://cdn-fastly.deb.debian.org/debian jessie main" > /etc/apt/sources.list.d/jessie.list
RUN echo "deb [check-valid-until=no] http://archive.debian.org/debian jessie-backports main" > /etc/apt/sources.list.d/jessie-backports.list
RUN sed -i '/deb http:\/\/deb.debian.org\/debian jessie-updates main/d' /etc/apt/sources.list
RUN apt-get -o Acquire::Check-Valid-Until=false update \
    && apt-get install --yes --no-install-recommends \
    libssl-dev \
    wget \
    vim \
    php5-mysql \
    && apt-get clean

RUN docker-php-ext-install mbstring \
    && docker-php-ext-install mysql

RUN wget https://pecl.php.net/get/mongo-1.6.16.tgz \
    && tar xzf mongo-1.6.16.tgz \
    && cd mongo-1.6.16 \
    && phpize \
    && ./configure \
    && make \
    && make install \
    #&& echo "extension=mongo.so" > /usr/local/etc/php/php.ini \
    && docker-php-ext-enable mongo

COPY phantomjs-2.1.1-linux-x86_64.tar.bz2 /tmp
# install phantomjs
RUN apt-get install --yes --no-install-recommends \
    libfreetype6 \
    libfontconfig1 \
    && apt-get clean \
    && cd /tmp \
    && tar xvjf phantomjs-2.1.1-linux-x86_64.tar.bz2 \
    && mv phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/bin \
    && rm -rf phantomjs*

# install mutt
RUN apt-get -o Acquire::Check-Valid-Until=false update \
    && apt-get install --yes --no-install-recommends \
    mutt \
    libsasl2-2 sasl2-bin libsasl2-modules \
    && apt-get clean \
    && mkdir /var/www/.mutt \
    && chmod 777 /var/log

COPY colors /var/www/.mutt/
COPY .muttrc /var/www/

RUN chown -R www-data:www-data /var/www/.mutt /var/www/.muttrc

WORKDIR /var/www/html

COPY index.php .

RUN mkdir -p /data/src /data/discuz /data/phpbb /data/share \
    && ln -s /data/src/forum . \
    && ln -s /data/src/ottawa . \
    && ln -s /data/discuz . \
    && ln -s /data/discuz upload \
    && ln -s /data/share . \
    && ln -s /data/phpbb .
