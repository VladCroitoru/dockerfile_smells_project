#
# INFRA-DEBIAN-PHP Docker/Codeship Debian with Web Application Components
#
FROM debian:8
MAINTAINER Louie Miranda <lmiranda@gmail.com>

# ENV MYSQL_USER=mysql \
#     MYSQL_DATA_DIR=/var/lib/mysql \
#     MYSQL_RUN_DIR=/run/mysqld \
#     MYSQL_LOG_DIR=/var/log/mysql

#
# UPDATE AND INSTALLS
#
RUN \
    apt-get update && \
    apt-get -y install \
        nginx \
        curl \
        git \

        # PHP
        php5-fpm php5-cli php5-curl php5-intl php5-curl php5-mysql php5-mcrypt php5-common php5-memcached php5-json php5-dev \

        # && echo mysql-server mysql-server/root_password password password123 | debconf-set-selections \
        # && echo mysql-server mysql-server/root_password_again password password123 | debconf-set-selections \
        # mysql-client mysql-server \

        memcached \
        awscli \
        phpunit \

        # Compiler
        libpcre3-dev gcc make && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN curl -sS https://getcomposer.org/installer | php -- --filename=composer --install-dir=/usr/bin

#
# PHALCON 2.0.13
#
RUN /usr/bin/git clone git://github.com/phalcon/cphalcon.git && \
    cd cphalcon/build/ && \
    ./install && \
    cd /tmp && \
    /bin/rm -rfv /tmp/cphalcon/ && \
    /usr/bin/apt-get -y purge git php5-dev libpcre3-dev gcc make && apt-get -y autoremove && apt-get clean && rm -rf /var/lib/apt/lists/*
RUN /bin/echo 'extension=phalcon.so' >/etc/php5/mods-available/phalcon.ini

#RUN /usr/sbin/php5enmod phalcon
#WORKDIR /var/www/phalcon/public
#RUN /bin/echo '<html><body><h1>It works!</h1></body></html>' > /var/www/phalcon/public/index.html

#
# PORTS
#
EXPOSE 80
#EXPOSE 443
EXPOSE 3306
EXPOSE 9000

#
# DAEMONIZE / STARTUP
#
RUN sed -i '/daemonize /c daemonize = no' /etc/php5/fpm/php-fpm.conf && \
    sed -i '/^listen /c listen = 0.0.0.0:9000' /etc/php5/fpm/pool.d/www.conf && \
    sed -i 's/^listen.allowed_clients/;listen.allowed_clients/' /etc/php5/fpm/pool.d/www.conf

RUN service php5-fpm start
RUN service nginx start
# RUN service mysql-server start

ADD scripts /scripts
RUN chmod -R 755 /scripts
ENV PATH $PATH:/scripts

WORKDIR /var/www/vcard