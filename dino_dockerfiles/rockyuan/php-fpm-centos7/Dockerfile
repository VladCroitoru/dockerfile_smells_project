FROM centos:7

MAINTAINER "RockYuan" <RockYuan@gmail.com>

# Install required repos, update, and then install PHP-FPM
RUN yum -y install http://rpms.famillecollet.com/enterprise/remi-release-7.rpm && \
    yum update -y && \
    yum install --enablerepo=remi,remi-php56 -y \
        php-cli \
        php-fpm \
        php-opcache \
        php-dbg \
        php-gd \
        php-mbstring \
        php-pdo \
        php-mysqlnd \
        php-pecl-imagick \
        php-pecl-xdebug \
        php-pecl-memcached \
        php-process \
        php-xml \
        php-pecl-mongodb \
        php-pecl-redis \
        php-bcmath \
        php-pecl-swoole && \
    yum clean all

# Configure and secure PHP
RUN sed -i "s/;date.timezone =.*/date.timezone = Asia\/Hong_Kong/" /etc/php.ini && \
    sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php-fpm.conf && \
    sed -i "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/" /etc/php.ini && \
    sed -i "s/short_open_tag = Off/short_open_tag = On/" /etc/php.ini && \
    sed -i '/^listen = /clisten = 0.0.0.0:9000' /etc/php-fpm.d/www.conf && \
    sed -i '/^listen.allowed_clients/c;listen.allowed_clients =' /etc/php-fpm.d/www.conf && \
    sed -i '/^;catch_workers_output/ccatch_workers_output = yes' /etc/php-fpm.d/www.conf && \
    sed -i "s/php_admin_flag\[log_errors\] = .*/;php_admin_flag[log_errors] =/" /etc/php-fpm.d/www.conf && \
    sed -i "s/php_admin_value\[error_log\] =.*/;php_admin_value[error_log] =/" /etc/php-fpm.d/www.conf && \
    sed -i "s/php_admin_value\[error_log\] =.*/;php_admin_value[error_log] =/" /etc/php-fpm.d/www.conf && \
    sed -i '/^php_value\[soap.wsdl_cache_dir\]/c;php_value[soap.wsdl_cache_dir] = ' /etc/php-fpm.d/www.conf && \
    echo "php_admin_value[display_errors] = 'stderr'" >> /etc/php-fpm.d/www.conf

# DATA VOLUMES
RUN mkdir -p /data/nginx/www
VOLUME ["/data/nginx/www"]

# PORTS
# Port 9000 is how Nginx will communicate with PHP-FPM.
EXPOSE 9000

# Run PHP-FPM on container start.
ENTRYPOINT ["/usr/sbin/php-fpm", "-F"]
