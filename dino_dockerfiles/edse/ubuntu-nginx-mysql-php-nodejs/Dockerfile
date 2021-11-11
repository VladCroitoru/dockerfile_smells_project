FROM ubuntu:14.04
MAINTAINER Emerson Estrella <emerson.estrella@gmail.com>

RUN DEBIAN_FRONTEND=noninteractive

# Update apt-get local index
RUN apt-get -qq update

# Install
RUN apt-get -y --force-yes install wget curl git unzip supervisor g++ make nginx mysql-server mysql-client redis-server php5-cli php5-fpm php5-dev php5-mysql php5-curl php5-intl php5-mcrypt php5-memcache php5-imap php5-sqlite

RUN bash -c "wget http://getcomposer.org/composer.phar && mv composer.phar /usr/local/bin/composer && chmod +x /usr/local/bin/composer"

# PHP Redis
RUN mkdir -p /tmp/php-redis
WORKDIR /tmp/php-redis
RUN wget https://github.com/phpredis/phpredis/archive/2.2.5.zip; unzip 2.2.5.zip
WORKDIR /tmp/php-redis/phpredis-2.2.5
RUN /usr/bin/phpize; ./configure; make; make install
RUN echo "extension=redis.so" > /etc/php5/mods-available/redis.ini
RUN php5enmod redis

# Node
RUN mkdir -p /tmp/node
WORKDIR /tmp/node
ENV NODE_VERSION 0.10.35
ENV NPM_VERSION 2.2.0
RUN curl -SLO "http://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.gz" \
    && tar -xzf "node-v$NODE_VERSION-linux-x64.tar.gz" -C /usr/local --strip-components=1 \
    && rm "node-v$NODE_VERSION-linux-x64.tar.gz" \
    && npm install -g npm@"$NPM_VERSION" \
    && npm cache clear \
    && rm -rf /tmp/*

# MySQL conf
RUN sed -i -e"s/^bind-address\s*=\s*127.0.0.1/bind-address = 0.0.0.0/" /etc/mysql/my.cnf

# PHP conf
RUN sed -i "s/;date.timezone =.*/date.timezone = UTC/" /etc/php5/fpm/php.ini
RUN sed -i "s/;date.timezone =.*/date.timezone = UTC/" /etc/php5/cli/php.ini
RUN sed -i "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/" /etc/php5/fpm/php.ini
RUN sed -i "s/;daemonize = yes/daemonize = no/" /etc/php5/fpm/php-fpm.conf

# nginx conf
RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf

ADD files/default /etc/nginx/sites-available/default
ADD files/supervisord.conf /etc/supervisor/supervisord.conf
ADD files/php-fpm.conf /etc/php5/fpm/php-fpm.conf
ADD files/start.sh /usr/local/bin/start.sh

RUN mkdir -p /tmp/node
WORKDIR /var/multrix
RUN chown www-data:www-data /var/multrix
RUN service mysql start && service redis-server start && mysql -e "create database tickets"

# Expose ports
EXPOSE 80
EXPOSE 443

# Default command for container, start supervisor
CMD ["supervisord", "--nodaemon"]
CMD ["service", "mysql", "start"]
CMD ["service", "redis-server", "start"]
CMD ["service", "php5-fpm", "start"]
CMD ["service", "nginx", "start"]
CMD ["/usr/local/bin/start.sh"]
