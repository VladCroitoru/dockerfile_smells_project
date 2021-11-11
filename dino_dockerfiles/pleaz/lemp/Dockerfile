FROM debian:stretch-slim
MAINTAINER Anton Kuk "oprstfaq@gmail.com"

# Set frontend. We'll clean this later on!
ENV DEBIAN_FRONTEND noninteractive

# Locale
ENV LOCALE en_US.UTF-8

# PHP Timezone
ENV TZ=Europe/Moscow

# Set repositories
RUN apt-get -qq update && apt-get -qqy upgrade

# Install some basic tools needed for deployment
RUN apt-get -yqq install \
  apt-utils \
  debconf \
  dialog \
  locales \
  gnupg2 \
  curl \
  wget \
  lsb-release \
  supervisor \
  openssl \
  aptitude \
  nano \
  htop \
  mc

# Install locale
RUN ln -s /etc/locale.alias /usr/share/locale/locale.alias
RUN \
  sed -i -e "s/# $LOCALE/$LOCALE/" /etc/locale.gen && \
  echo "LANG=$LOCALE">/etc/default/locale && \
  dpkg-reconfigure --frontend=noninteractive locales && \
  update-locale LANG=$LOCALE

# Install PHP7
RUN aptitude install -y php7.0-fpm php7.0-mysql php7.0-curl php7.0-gd php7.0-intl php7.0-imap php7.0-json php7.0-mcrypt php7.0-pspell php7.0-recode php7.0-sqlite3 php7.0-tidy php7.0-xml php7.0-xmlrpc php7.0-xsl php7.0-mbstring php7.0-opcache php7.0-zip php7.0-bz2 php-memcache php-gettext php-pear php-imagick php-apcu
RUN mkdir -p /var/run/php
COPY www.conf /etc/php/7.0/fpm/pool.d/
COPY php.ini /etc/php/7.0/fpm/

# PHP Timezone
RUN \
  echo $TZ | tee /etc/timezone && \
  dpkg-reconfigure --frontend noninteractive tzdata && \
  echo "date.timezone = \"$TZ\";" > /etc/php/7.0/fpm/conf.d/timezone.ini

# PHP IonCube
RUN \
  wget https://downloads.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64.tar.gz && \
  tar xvfz ioncube_loaders_lin_x86-64.tar.gz && \
  cp ioncube/ioncube_loader_lin_7.0.so /usr/lib/php/20151012/ && \
  echo "zend_extension = \"/usr/lib/php/20151012/ioncube_loader_lin_7.0.so\"" > /etc/php/7.0/fpm/conf.d/00-ioncube.ini && \
  rm ioncube_loaders_lin_x86-64.tar.gz && \
  rm -rf ioncube_loaders_lin_x86-64

# Install NGINX
RUN curl -O https://nginx.ru/keys/nginx_signing.key
RUN apt-key add nginx_signing.key
RUN echo "deb http://nginx.org/packages/mainline/debian/ stretch nginx" >> /etc/apt/sources.list \
    && echo "deb-src http://nginx.org/packages/mainline/debian/ stretch nginx" >> /etc/apt/sources.list
RUN aptitude update && aptitude install -y nginx
COPY default.conf /etc/nginx/conf.d/
COPY nginx.conf /etc/nginx/

# NGINX logs
RUN ln -sf /dev/stdout /var/log/nginx/access.log && \
	ln -sf /dev/stderr /var/log/nginx/error.log

# Install MySql
RUN wget -O /tmp/RPM-GPG-KEY-mysql https://repo.mysql.com/RPM-GPG-KEY-mysql
RUN apt-key add /tmp/RPM-GPG-KEY-mysql
RUN echo "deb http://repo.mysql.com/apt/debian/ stretch mysql-8.0" >> /etc/apt/sources.list.d/mysql.list \
    && echo "deb-src http://repo.mysql.com/apt/debian/ stretch mysql-8.0" >> /etc/apt/sources.list.d/mysql.list
RUN { \
        echo mysql-community-server mysql-community-server/data-dir select '/var/lib/mysql'; \
        echo mysql-community-server mysql-community-server/root-pass password '48115'; \
        echo mysql-community-server mysql-community-server/re-root-pass password '48115'; \
        echo mysql-community-server mysql-community-server/remove-test-db select false; \
    } | debconf-set-selections \
    && aptitude update && aptitude install -y mysql-server
COPY mysqld.cnf /etc/mysql/mysql.conf.d/

# Install Memcached
RUN aptitude install -y memcached

# Install PhpMyAdmin
#RUN mysqld -u mysql & aptitude install -y phpmyadmin
RUN aptitude install -y phpmyadmin
RUN dpkg-reconfigure phpmyadmin

# Clean packages
RUN aptitude clean
RUN rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*

# Cfg supervisor
COPY supervisord.conf /etc/supervisor/conf.d/daemons.conf

# Working dir
WORKDIR /var/www/html

# Volume for www & mysql data
VOLUME ["/var/www/html"]
#VOLUME ["/var/lib/mysql"]

EXPOSE 80

ENTRYPOINT ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/daemons.conf"]