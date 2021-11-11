FROM ubuntu:16.04
MAINTAINER khanhicetea@gmail.com
RUN apt-get clean && apt-get -y update && apt-get install -y locales curl software-properties-common git \
  && locale-gen en_US.UTF-8
RUN LC_ALL=en_US.UTF-8 add-apt-repository ppa:ondrej/php
RUN apt-get update
RUN apt-get install -y --force-yes php7.1-bcmath php7.1-bz2 php7.1-cli php7.1-common libapache2-mod-php7.1 php7.1-curl \
                php7.1-cgi php7.1-dev php7.1-fpm php7.1-gd php7.1-gmp php7.1-imap php7.1-intl \
                php7.1-json php7.1-ldap php7.1-mbstring php7.1-mcrypt php7.1-mysql \
                php7.1-odbc php7.1-opcache php7.1-pgsql php7.1-phpdbg php7.1-pspell \
                php7.1-readline php7.1-recode php7.1-soap php7.1-sqlite3 \
                php7.1-tidy php7.1-xml php7.1-xmlrpc php7.1-xsl php7.1-zip \
                php-tideways php-mongodb libevent-dev php-imagick php-memcached php-redis

RUN sed -i "s/;date.timezone =.*/date.timezone = UTC/" /etc/php/7.1/cli/php.ini
RUN sed -i "s/;date.timezone =.*/date.timezone = UTC/" /etc/php/7.1/fpm/php.ini
RUN sed -i "s/display_errors = Off/display_errors = On/" /etc/php/7.1/fpm/php.ini
RUN sed -i "s/upload_max_filesize = .*/upload_max_filesize = 10M/" /etc/php/7.1/fpm/php.ini
RUN sed -i "s/post_max_size = .*/post_max_size = 12M/" /etc/php/7.1/fpm/php.ini
RUN sed -i "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/" /etc/php/7.1/fpm/php.ini
RUN sed -i -e "s/pid =.*/pid = \/var\/run\/php7.1-fpm.pid/" /etc/php/7.1/fpm/php-fpm.conf
RUN mkdir /var/log/php-fpm
RUN sed -i -e "s/error_log =.*/error_log = \/var\/log\/php-fpm\/fpm-error.log/" /etc/php/7.1/fpm/php-fpm.conf
RUN sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php/7.1/fpm/php-fpm.conf
RUN sed -i "s/listen = .*/listen = 9000/" /etc/php/7.1/fpm/pool.d/www.conf
RUN sed -i "s/;catch_workers_output = .*/catch_workers_output = yes/" /etc/php/7.1/fpm/pool.d/www.conf

RUN curl https://getcomposer.org/installer > composer-setup.php && php composer-setup.php && mv composer.phar /usr/local/bin/composer && rm composer-setup.php
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN apt-get update && apt-get install -y libssl-dev pkg-config
RUN apt-get install -y libmagickwand-dev --no-install-recommends

RUN apt-get install -y php-dev
RUN apt-get install -y wget
RUN cd /tmp
RUN wget https://pecl.php.net/get/imagick-3.4.3RC1.tgz
RUN tar xvzf imagick-3.4.3RC1.tgz
RUN cd imagick-3.4.3RC1 \
&& phpize \
&& ./configure \
&& make install
RUN rm -rf /tmp/imagick-3.4.3RC1*
RUN service php7.1-fpm restart

RUN chown -R www-data:www-data /var/www

WORKDIR /var/www/html

CMD ["php-fpm7.1"]

EXPOSE 9000