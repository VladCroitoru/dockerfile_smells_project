FROM ubuntu:12.04

MAINTAINER AJ <aj@laatu.uk>

RUN apt-get update
RUN apt-get -y install apache2 bc build-essential clamav curl ghostscript \
    libapache2-mod-php5 libapache2-mod-rpaf libapache2-modsecurity libcurl3 \
    mysql-client-core-5.5 php-apc php-pear php5 php5-cli php5-common php5-curl \
    php5-dev php5-gd php5-intl php5-mcrypt php5-mysql php5-tidy php5-xdebug \
    php5-xsl rsync wget zip

RUN apt-get clean

RUN mkdir -p /app
COPY index.php /app/

COPY php.ini /etc/php5/apache2/conf.d/

RUN a2dismod alias
RUN a2enmod expires headers rewrite unique_id

COPY apphost /etc/apache2/sites-available/
RUN a2dissite default
RUN a2ensite apphost

RUN update-rc.d apache2 defaults

EXPOSE 80

CMD ["/usr/sbin/apachectl", "-D", "FOREGROUND"]