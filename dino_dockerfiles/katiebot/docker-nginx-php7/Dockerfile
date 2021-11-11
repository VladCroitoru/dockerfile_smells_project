# Use the latest Ubuntu base image
FROM ubuntu:trusty
MAINTAINER Katie Graham katie@webscope.co.nz

ENV TERM xterm

# Let the conatiner know that there is no tty
ENV DEBIAN_FRONTEND noninteractive

# Set the locale
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# apt-get
RUN apt-get update -qqy && apt-get install -qqy software-properties-common python-software-properties

# Add colours to bashrc
RUN  sed -i -e "s/#force_color_prompt=yes/force_color_prompt=yes/g" /root/.bashrc

# Install nginx
RUN nginx=stable && \
    add-apt-repository ppa:nginx/$nginx && \
    apt-get update && \
    apt-get install -qqy nginx

# Install php7 packages
RUN add-apt-repository -y ppa:ondrej/php-7.0 && apt-get update -qqy && \
    apt-get install -qqy \
    php7.0-fpm \
    php7.0-cli \
    php7.0-common \
    php7.0-curl \
    php7.0-json \
    php7.0-gd \
    php7.0-mcrypt \
    php7.0-odbc \
    php7.0-pgsql \
    php7.0-mysql \
    php7.0-xmlrpc \
    php7.0-opcache \
    php7.0-intl \
    php7.0-bz2

# Install other software
RUN apt-get install -qqy \
    python-setuptools \
    curl \
    mysql-client \
    git \
    vim \
    supervisor \
    sendmail

# tweak nginx config
RUN sed -i -e "s/worker_processes  1/worker_processes 5/" /etc/nginx/nginx.conf && \
    sed -i -e "s/keepalive_timeout\s*65/keepalive_timeout 2/" /etc/nginx/nginx.conf && \
    sed -i -e "s/keepalive_timeout 2/keepalive_timeout 2;\n\tclient_max_body_size 100m/" /etc/nginx/nginx.conf && \
    echo "daemon off;" >> /etc/nginx/nginx.conf

# tweak php-fpm config
RUN sed -i -e "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g" /etc/php/7.0/fpm/php.ini && \
    sed -i -e "s/upload_max_filesize\s*=\s*2M/upload_max_filesize = 100M/g" /etc/php/7.0/fpm/php.ini && \
    sed -i -e "s/post_max_size\s*=\s*8M/post_max_size = 100M/g" /etc/php/7.0/fpm/php.ini && \
    sed -i -e "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g" /etc/php/7.0/cli/php.ini && \
    sed -i -e "s/upload_max_filesize\s*=\s*2M/upload_max_filesize = 100M/g" /etc/php/7.0/cli/php.ini && \
    sed -i -e "s/post_max_size\s*=\s*8M/post_max_size = 100M/g" /etc/php/7.0/cli/php.ini && \
    sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php/7.0/fpm/php-fpm.conf && \
    sed -i -e "s/;catch_workers_output\s*=\s*yes/catch_workers_output = yes/g" /etc/php/7.0/fpm/pool.d/www.conf && \
    sed -i -e "s/pm.max_children = 5/pm.max_children = 9/g" /etc/php/7.0/fpm/pool.d/www.conf && \
    sed -i -e "s/pm.start_servers = 2/pm.start_servers = 3/g" /etc/php/7.0/fpm/pool.d/www.conf && \
    sed -i -e "s/pm.min_spare_servers = 1/pm.min_spare_servers = 2/g" /etc/php/7.0/fpm/pool.d/www.conf && \
    sed -i -e "s/pm.max_spare_servers = 3/pm.max_spare_servers = 4/g" /etc/php/7.0/fpm/pool.d/www.conf && \
    sed -i -e "s/pm.max_requests = 500/pm.max_requests = 200/g" /etc/php/7.0/fpm/pool.d/www.conf

# fix ownership of sock file for php-fpm
RUN sed -i -e "s/;listen.mode = 0660/listen.mode = 0750/g" /etc/php/7.0/fpm/pool.d/www.conf && \
    find /etc/php/7.0/cli/conf.d/ -name "*.ini" -exec sed -i -re 's/^(\s*)#(.*)/\1;\2/g' {} \;

# nginx site conf
RUN rm -Rf /etc/nginx/conf.d/* && \
    rm -Rf /etc/nginx/sites-available/default && \
    mkdir -p /etc/nginx/ssl/
ADD ./nginx-site.conf /etc/nginx/sites-available/default.conf
RUN ln -s /etc/nginx/sites-available/default.conf /etc/nginx/sites-enabled/default.conf

# Install composer
RUN curl -sS https://getcomposer.org/installer | php && \
    mv composer.phar /usr/local/bin/composer && \
    composer global require hirak/prestissimo

# Install drush
RUN composer global require drush/drush && \
    ln -s /root/.composer/vendor/bin/drush /usr/bin/drush

# Install drupal console
RUN curl https://drupalconsole.com/installer -L -o drupal.phar && \
    mv drupal.phar /usr/local/bin/drupal && \
    chmod +x /usr/local/bin/drupal

# Install terminus
RUN curl https://github.com/pantheon-systems/cli/releases/download/0.7.1/terminus.phar -L -o terminus.phar && \
    mv terminus.phar /usr/local/bin/terminus && \
    chmod +x /usr/local/bin/terminus

# Supervisor Config
ADD ./supervisord.conf /etc/supervisord.conf

# Start Supervisord
ADD ./start.sh /start.sh
RUN chmod 755 /start.sh

RUN usermod -u 1000 www-data
RUN usermod -a -G users www-data

RUN mkdir -p /var/www/html
RUN chown -R www-data:www-data /var/www

# add test PHP file
ADD ./index.php /var/www/html/index.php

RUN mkdir /run/php && chown www-data:www-data -R /run/php

WORKDIR /var/www/html

# Expose Ports
EXPOSE 443
EXPOSE 80

CMD ["/bin/bash", "/start.sh"]
