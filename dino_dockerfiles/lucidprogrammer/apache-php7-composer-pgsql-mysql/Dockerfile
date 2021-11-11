FROM ubuntu:16.04
MAINTAINER Lucid Programmer<lucidprogrammer@hotmail.com>

ENV PATH $PATH:/root/.composer/vendor/bin
# by default give a DocumentRoot
ENV DOCUMENT_ROOT /var/www/html
ENV PORT 80

RUN apt-get update && \
    apt-get dist-upgrade -y && \
    apt-get install -y \
      apache2 \
      mcrypt \
      php7.0 \
      php7.0-cli \
      libapache2-mod-php7.0 \
      php7.0-gd \
      php7.0-json \
      php7.0-ldap \
      php7.0-mbstring \
      php7.0-mysql \
      php7.0-pgsql \
    # php7.0-sqlite3 \
      php7.0-xml \
      php7.0-xsl \
      php7.0-zip \
      php7.0-curl \
      php7.0-mcrypt
RUN apt-get install -y curl
# Next composer and global composer package, as their versions may change from time to time
RUN curl -sS https://getcomposer.org/installer | php \
    && mv composer.phar /usr/local/bin/composer.phar


# Apache config and composer wrapper
COPY apache2.conf /etc/apache2/apache2.conf
COPY composer /usr/local/bin/composer
RUN chmod +x /usr/local/bin/composer
WORKDIR /var/www/html

COPY run /usr/local/bin/run
RUN chmod +x /usr/local/bin/run
RUN a2enmod rewrite


CMD ["/usr/local/bin/run"]
