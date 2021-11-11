FROM nimmis/apache:14.04
MAINTAINER creecros <creecros@gmail.com>                                                                                                                 

# disable interactive functions
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
apt-get install -y php5 libapache2-mod-php5  \
php5-fpm php5-cli php5-mysqlnd php5-pgsql php5-sqlite php5-redis \
php5-apcu php5-intl php5-imagick php5-ldap php5-mcrypt php5-json php5-gd php5-curl && \
php5enmod mcrypt && \
rm -rf /var/lib/apt/lists/* && \
cd /tmp && curl -sS https://getcomposer.org/installer | php && mv composer.phar /usr/local/bin/composer

RUN wget http://ltb-project.org/archives/ltb-project-self-service-password-1.1.tar.gz && \
tar zxvf ltb-project-self-service-password-1.1.tar.gz && \
mv ltb-project-self-service-password-1.1 /var/www && \
rm -r /var/www/html && \
mv /var/www/ltb-project-self-service-password-1.1 /var/www/html && \
rm ltb-project-self-service-password-1.1.tar.gz
