# vim-set ft=dockerfile-
FROM ubuntu:16.04

# install nginx php-fpm 
RUN apt-get update \
    && apt-get install -y debconf-utils \
    && apt-get install -y nginx \
    && apt-get install -y php-fpm php-mysql

# install percona-server 
RUN apt-get update \
    && { \
        echo mysql-server-5.7 mysql-server/root_password password 'root'; \
        echo mysql-server-5.7 mysql-server/root_password_again password 'root'; \
    } | debconf-set-selections \
    && apt-get install -y mysql-server-5.7

# install supervisor redis
RUN apt-get install -y supervisor redis-server

# clean
RUN apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/*

# Configure NGINX to run properly on docker
RUN sed -i "/access_log .*/c\\\taccess_log /proc/self/fd/2;" /etc/nginx/nginx.conf \
    && sed -i "/error_log .*/c\\\terror_log /proc/self/fd/2;" /etc/nginx/nginx.conf

# Configure FPM to run properly on docker
RUN sed -i "/listen = .*/c\listen = [::]:9000" /etc/php/7.0/fpm/pool.d/www.conf \
    && sed -i "/;access.log = .*/c\access.log = /proc/self/fd/2" /etc/php/7.0/fpm/pool.d/www.conf \
    && sed -i "/;clear_env = .*/c\clear_env = no" /etc/php/7.0/fpm/pool.d/www.conf \
    && sed -i "/;catch_workers_output = .*/c\catch_workers_output = yes" /etc/php/7.0/fpm/pool.d/www.conf \
    && sed -i "/pid = .*/c\;pid = /run/php/php7.0-fpm.pid" /etc/php/7.0/fpm/php-fpm.conf \
    && sed -i "/;daemonize = .*/c\daemonize = no" /etc/php/7.0/fpm/php-fpm.conf \
    && sed -i "/error_log = .*/c\error_log = /proc/self/fd/2" /etc/php/7.0/fpm/php-fpm.conf \
    && usermod -u 1000 www-data

# Configure Redis to run properly on docker
RUN sed -i "/daemonize yes.*/c\daemonize no" /etc/redis/redis.conf \
    && sed -i "/bind 127.0.0.1/c\bind 0.0.0.0" /etc/redis/redis.conf

# Allow root remote connect
RUN service mysql start \
    && mysql -uroot -proot -e "update mysql.user set Host = '%' where User='root';" \
    && echo "bind-address = 0.0.0.0" >> /etc/mysql/conf.d/mysql.cnf

VOLUME ["/var/www", "/etc/nginx/sites-enabled"]

EXPOSE 80 3306 6379 9000

# copy supervisor conf
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# start supervisor
CMD ["/usr/bin/supervisord"]




