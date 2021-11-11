#UBUNTU
FROM ubuntu:latest
RUN apt-get update

#APACHE
RUN apt-get -y install apache2
RUN apt-get -y install libapache2-mod-php7.0 php7.0 php7.0-cli php-xdebug php7.0-mbstring sqlite3 php7.0-mysql \
    php-imagick php-memcached php-pear curl imagemagick php7.0-dev php7.0-phpdbg php7.0-gd php7.0-zip php7.0-curl \
    npm nodejs php7.0-json php7.0-curl php7.0-sqlite3 php7.0-intl apache2 wget libsasl2-dev libssl-dev \
    libsslcommon2-dev libcurl4-openssl-dev openssl libssl-dev libcurl4-openssl-dev pkg-config libsasl2-dev libpcre3-dev \
  && a2enmod headers \
  && a2enmod rewrite \
  && curl -sS https://getcomposer.org/installer | php \
  && mv composer.phar /usr/local/bin/composer.phar \
  && alias composer='/usr/local/bin/composer.phar'

ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_PID_FILE /var/run/apache2.pid
ENV APACHE_RUN_DIR /var/run/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2
RUN ln -sf /dev/stdout /var/log/apache2/access.log && \
    ln -sf /dev/stderr /var/log/apache2/error.log
RUN mkdir -p $APACHE_RUN_DIR $APACHE_LOCK_DIR $APACHE_LOG_DIR

#MYSQL
RUN echo "mysql-server-5.5 mysql-server/root_password password password" | debconf-set-selections
RUN echo "mysql-server-5.5 mysql-server/root_password_again password password" | debconf-set-selections
RUN apt-get -y install mysql-server

#COPY PROJECT
COPY . /var/www/html
COPY ./apache.conf /etc/apache2/sites-available/000-default.conf

#ENTRY
WORKDIR /var/www/html
EXPOSE 80

#NPM AND COMPOSER
RUN npm config set registry http://registry.npmjs.org && npm install
RUN /usr/local/bin/composer.phar install

#DATABASE
RUN service mysql start \
    && mysql -u root -ppassword -e "CREATE DATABASE IF NOT EXISTS cocoturbo;" \
    && php artisan migrate \
    && php artisan db:seed

CMD ["bash", "run.sh"]