############################################################
# Dockerfile to build joomla Installed Containers
# Based on Ubuntu
############################################################

FROM gjong/apache

MAINTAINER Christian Heimke <c.heimke@loumaris.com>

RUN apt-get install -y git


RUN rm -rf /var/www/*

VOLUME ["/var/www"]

RUN chown www-data:www-data /var/www -R
RUN a2enmod rewrite

ADD ./config/file_limit.conf /etc/apache2/conf-enabled/file_limit.conf
ADD ./config/000-default.conf /etc/apache2/sites-enabled/000-default.conf
ADD ./config/htaccess /var/www/.htaccess

EXPOSE 80

CMD ["/bin/bash", "/start.sh"]
