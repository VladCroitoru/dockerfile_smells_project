FROM debian:jessie
MAINTAINER Herlon Aguiar <herlon214@gmail.com>

VOLUME ["/var/www"]

WORKDIR /var/www

RUN apt-get update && \
    apt-get install -y \
      curl \
      git-core \
      locales \
      apache2 \
      php5 \
      php5-cli \
      libapache2-mod-php5 \
      php5-curl \
      php5-gd \
      php5-json \
      php5-ldap \
      php5-mysql \
      php5-pgsql

COPY apache_default /etc/apache2/sites-available/000-default.conf
COPY php.ini /etc/php5/apache2/php.ini
COPY run /usr/local/bin/run
RUN chmod +x /usr/local/bin/run
RUN a2enmod rewrite

EXPOSE 80
CMD ["/usr/local/bin/run"]
