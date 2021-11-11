FROM debian:wheezy

# Variables d'environnement
ENV DEBIAN_FRONTEND noninteractive
ENV INITRD No

# sources.list fr
RUN echo "deb http://ftp.fr.debian.org/debian wheezy main" > /etc/apt/sources.list
RUN echo "deb http://ftp.fr.debian.org/debian wheezy-updates main"  >> /etc/apt/sources.list
RUN echo "deb http://security.debian.org wheezy/updates main" >> /etc/apt/sources.list
RUN apt-get update --fix-missing

# HHVM
# RUN apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0x5a16e7281be7a449
# RUN echo deb http://dl.hhvm.com/debian wheezy main | tee /etc/apt/sources.list.d/hhvm.list
# RUN apt-get update --fix-missing
# RUN apt-get install -y hhvm
# RUN echo 'hhvm.libxml.ext_entity_whitelist = file,http' >> /etc/hhvm/php.ini
# RUN echo 'date.timezone = "Europe/Paris"' >> /etc/hhvm/php.ini

# Dependencies
RUN apt-get install -y apt-utils debconf-utils dialog locales
RUN apt-get install -y nginx wget git python build-essential curl bzip2 vim nano \
  php5 phpunit php5-fpm php5-mysql php5-imagick php5-curl php5-intl php-apc acl adduser supervisor net-tools 

# composer
RUN cd /usr/local/sbin/ && curl -sS https://getcomposer.org/installer | php && mv composer.phar composer

# nginx
COPY nginx.conf /etc/nginx/sites-enabled/default

# silex
COPY composer.json /var/www/composer.json
RUN mkdir /var/www/web
RUN cd /var/www/web && wget http://gist.github.com/jcherqui/1ae342ab2cc43de975c3/raw/e7523947993b542438f4d59e91ce66935fa64c9a/index.php
RUN cd /var/www/ && composer install

# start
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php5/fpm/php-fpm.conf
RUN mkdir -p /var/log/supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
CMD ["/usr/bin/supervisord", "-n"]

EXPOSE 80

