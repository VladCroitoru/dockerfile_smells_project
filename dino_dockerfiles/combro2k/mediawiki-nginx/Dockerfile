# Mediawiki-Nginx
#
# Version 1.0
FROM ubuntu-debootstrap:14.04
MAINTAINER Martijn van Maurik <docker@vmaurik.nl>

# Ensure UTF-8
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys ABF5BD827BD9BF62
RUN echo deb http://nginx.org/packages/mainline/ubuntu trusty nginx > /etc/apt/sources.list.d/nginx-stable-trusty.list
RUN apt-get update
RUN apt-get -y upgrade

# Install
RUN apt-get install -y nginx \
    php5-fpm php5-mysql php-apc php5-imagick php5-imap php5-mcrypt php5-gd libssh2-php git php5-curl

RUN mkdir -p /etc/nginx/sites-enabled

RUN echo "cgi.fix_pathinfo = 0;" >> /etc/php5/fpm/php.ini
ADD nginx.conf /etc/nginx/nginx.conf
ADD nginx-site.conf /etc/nginx/sites-enabled/default
RUN sed -i -e 's/^listen =.*/listen = \/var\/run\/php5-fpm.sock/' /etc/php5/fpm/pool.d/www.conf

RUN mkdir -p /etc/nginx/scripts
ADD proxy_client_ip.php /etc/nginx/scripts/proxy_client_ip.php

# Remove the old hello world app and grab Mediawiki source
RUN git clone https://gerrit.wikimedia.org/r/p/mediawiki/core.git /data
RUN chown -R www-data:www-data /data

# Create the section for persistent files
RUN mkdir /var/lib/mediawiki

# Move the files that need to be persistent and create symbolic links to them
RUN mv /data/images /var/lib/mediawiki/ && ln -s /var/lib/mediawiki/images /data/images
RUN mv /data/skins /var/lib/mediawiki/ && ln -s /var/lib/mediawiki/skins /data/skins
RUN touch /var/lib/mediawiki/LocalSettings.php && ln -s /var/lib/mediawiki/LocalSettings.php /data/LocalSettings.php

VOLUME ["/var/lib/mediawiki/"]

EXPOSE 80
ADD start.sh /start.sh
RUN chmod +x /start.sh
CMD ["/start.sh"]
