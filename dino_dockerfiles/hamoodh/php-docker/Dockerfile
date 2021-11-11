FROM ubuntu:12.04
MAINTAINER PHP <hamoodh@xerago.com>

# Install packages
RUN apt-get update && \
 DEBIAN_FRONTEND=noninteractive apt-get -y upgrade && \
 DEBIAN_FRONTEND=noninteractive apt-get -y install supervisor pwgen && \
 apt-get -y install git apache2 libapache2-mod-php5 php5-mysql php5-pgsql php5-gd php-pear php-apc curl && \
 curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin && \
 mv /usr/local/bin/composer.phar /usr/local/bin/composer

# Override default apache conf
ADD apache.conf /etc/apache2/sites-enabled/000-default.conf

# Enable apache rewrite module
RUN a2enmod rewrite

# Add image configuration and scripts
ADD start.sh /start.sh
ADD run.sh /run.sh
RUN chmod 755 /*.sh
ADD supervisord-apache2.conf /etc/supervisor/conf.d/supervisord-apache2.conf

# Configure /app folder
#RUN mkdir -p /app && rm -fr /var/www/html && ln -s /app /var/www/html
RUN mkdir -p /var/www/html/
COPY app/ /var/www/html/

EXPOSE 80
CMD ["/run.sh"]
