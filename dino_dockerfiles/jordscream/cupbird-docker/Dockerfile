FROM php:5.5-apache

RUN sed -i 's/\/var\/www/\/var\/docker\/sources/g' /etc/apache2/apache2.conf \
    && sed -i 's/\/html/\/web/g' /etc/apache2/apache2.conf

RUN a2enmod rewrite \
    && apt-get update \
    && echo mysql-server mysql-server/root_password password docker | debconf-set-selections \
    && echo mysql-server mysql-server/root_password_again password docker | debconf-set-selections \
    && apt-get install -y libpng12-dev libjpeg-dev libpq-dev mysql-server git drush gzip vim wget zip default-jre libxml2-dev ruby-compass php5-curl \
    && docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \
    && docker-php-ext-install gd mbstring pdo pdo_mysql pdo_pgsql soap \
    && a2ensite 000-default \
    && apt-get clean && apt-get purge

ADD php.ini /usr/local/etc/php/php.ini
ADD my.cnf /etc/mysql/my.cnf

EXPOSE 3306

RUN mkdir -p /var/docker
WORKDIR /var/docker/sources

RUN apt-get update && apt-get install -y php-pear libssh2-php php5-ssh2  \
    && curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin

ADD run.sh /tmp/run.sh
RUN chmod 755 /tmp/run.sh
CMD ["/tmp/run.sh"]


