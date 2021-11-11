#FROM ubuntu:trusty
FROM azukiapp/node:0.12
MAINTAINER Junior Ribeiro


RUN apt-get -qq update 
RUN echo "deb http://ppa.launchpad.net/ondrej/php/ubuntu trusty main" >> /etc/apt/sources.list.d/php7.list  
RUN echo "deb-src http://ppa.launchpad.net/ondrej/php/ubuntu trusty main" >> /etc/apt/sources.list.d/php7.list  
#RUN add-apt-repository ppa:ondrej/php 
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E5267A6C 
RUN apt-get -qq update 

RUN apt-get install -y -qq \
php7.0 \
php7.0-fpm \
php7.0-mcrypt \
php7.0-mbstring \
php7.0-xml \
php7.0-pgsql \
php7.0-mysql \
php7.0-intl \
php7.0-curl \
php7.0-gd \
php7.0-json \
php7.0-xsl \
php7.0-cli \
php7.0-dev \
php-pear \
nginx \
npm \
curl \
git \
unzip \
libxml2 \
libcurl4-openssl-dev \
sqlite3 libsqlite3-dev \
subversion
#nodejs

#RUN curl -sS https://getcomposer.org/installer | sudo php -- --install-dir=/usr/local/bin --filename=composer
RUN npm install --save gulp-install 

RUN phpenmod mcrypt 


# nginx config
ADD nginx-default.conf /etc/nginx/sites-available/default
RUN  echo "daemon off;" >> /etc/nginx/nginx.conf \
  && echo "fix ownership of sock file for php-fpm as our version of nginx runs as root" \
  && sed -i -e "s/user www-data/user root/g" /etc/nginx/nginx.conf \
  && sed -i -e "s/www-data/root/g" /etc/php/7.0/fpm/pool.d/www.conf \
  && sed -i -e "s/;clear_env = no/clear_env = no/g" /etc/php/7.0/fpm/pool.d/www.conf \
  && sed -i -e "s/listen = \/run\/php\/php7.0-fpm.sock/listen = 127.0.0.1:9000/" /etc/php/7.0/fpm/pool.d/www.conf \
  && sed -i -e "s/DAEMON_ARGS=\"/DAEMON_ARGS=\"--allow-to-run-as-root /g" /etc/init.d/php7.0-fpm

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# Add image configuration and scripts
ADD run.sh /run.sh
RUN chmod 755 /*.sh

# Configure nginx root with sample app
ADD sample/ /var/www/public

EXPOSE 80
CMD ["/run.sh"]

