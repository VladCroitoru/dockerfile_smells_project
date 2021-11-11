FROM php:7.0-apache
MAINTAINER Lucid Programmer<lucidprogrammer@hotmail.com>
ENV PATH $PATH:/root/.composer/vendor/bin
# by default give a DocumentRoot
ENV DOCUMENT_ROOT /var/www/html
ENV PORT 80

RUN apt-get update && \
    apt-get install -y \
    # gd needs libpng-dev
    libpng-dev \
    # libldb-dev libldap2-dev are needed for ldap
    libldb-dev \
    libldap2-dev \
    # xsl needs this
    libxslt-dev \
    # curl
    libcurl4-gnutls-dev \
    # mcrypt needs (libmcrypt-dev libreadline-dev)
    libmcrypt-dev \
    libreadline-dev \
    # for pgsql
    libpq-dev \
    wget \
    vim


RUN ln -s /usr/lib/x86_64-linux-gnu/libldap.so /usr/lib/libldap.so \
    && ln -s /usr/lib/x86_64-linux-gnu/liblber.so /usr/lib/liblber.so
RUN docker-php-source extract && \
    curl -L -o /tmp/redis.tar.gz https://github.com/phpredis/phpredis/archive/3.1.1.tar.gz && \
    tar -zxf /tmp/redis.tar.gz && \
    rm -r /tmp/redis.tar.gz && \
    mv phpredis-3.1.1 /usr/src/php/ext/redis && \
    docker-php-ext-install gd json ldap mbstring pdo pdo_pgsql pgsql xml xsl zip curl mcrypt redis soap  && \
    docker-php-source delete

# install composer
RUN curl -sS https://getcomposer.org/installer | php \
    && mv composer.phar /usr/local/bin/composer.phar

COPY apache2.conf /etc/apache2/apache2.conf
COPY composer /usr/local/bin/composer
RUN chmod +x /usr/local/bin/composer
WORKDIR /var/www/html

RUN a2enmod rewrite
RUN echo "Alias /saml /var/www/html/vendor/simplesamlphp/simplesamlphp/www" >> /etc/apache2/apache2.conf
RUN echo "<Directory \"/var/www/html/vendor/simplesamlphp/simplesamlphp/www/\"> \n Options Indexes FollowSymLinks \n AllowOverride all \n Require all granted \n   </Directory>" >> /etc/apache2/apache2.conf
