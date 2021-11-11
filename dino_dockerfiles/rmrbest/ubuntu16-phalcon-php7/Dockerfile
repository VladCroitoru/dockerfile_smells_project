FROM ubuntu:16.04

RUN DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
    apt-get -y install apache2 git php7.0 gcc make re2c libpcre3-dev libapache2-mod-php7.0 mcrypt php7.0-mcrypt php7.0-json php7.0-dev php7.0-mysql php7.0-sqlite php7.0-bcmath && \
    apt-get autoremove && \
    rm -rf /var/lib/apt/lists/*

RUN a2enmod php7.0
RUN a2enmod rewrite

RUN sed -i "s/short_open_tag = Off/short_open_tag = On/" /etc/php/7.0/apache2/php.ini
#RUN sed -i "s/error_reporting = .*$/error_reporting = E_ERROR | E_WARNING | E_PARSE/" /etc/php5/apache2/php.ini

ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2
ENV APACHE_PID_FILE /var/run/apache2.pid

COPY 000-default.conf /etc/apache2/sites-available/000-default.conf

WORKDIR /tmp
RUN git clone --depth=1 https://github.com/phalcon/zephir.git \
    && find zephir -type f -print0 | xargs -0 sed -i 's/sudo //g' \
    && cd zephir \
    && ./install -c

WORKDIR /tmp
RUN git clone --branch 2.1.x --depth=1 https://github.com/phalcon/cphalcon.git \
    && cd cphalcon \
    && zephir fullclean \
    && zephir build --backend=ZendEngine3 \
    && echo "extension=phalcon.so" >> /etc/php/7.0/apache2/conf.d/30-phalcon.ini


EXPOSE 80

CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]