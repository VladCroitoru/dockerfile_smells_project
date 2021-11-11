# ------------------------------------------------------------------------------
# Based on a work at https://github.com/docker/docker.
# ------------------------------------------------------------------------------

FROM kdelfour/supervisor-docker
MAINTAINER Kevin Delfour <kevin@delfour.eu>

# Install base
RUN apt-get update && apt-get install -yq \
    fontconfig-config \
    fonts-dejavu-core \
    git \
    libgd-tools \
    libmcrypt-dev \
    mcrypt \
    mysql-client \
    mysql-server \
    nginx \
    php-pear \
    php5-cli \
    php5-common \
    php5-common \
    php5-fpm \
    php5-gd \
    php5-imagick \
    php5-json \
    php5-json \
    php5-mcrypt \
    php5-mysql \
    php5-readline \
    psmisc \
    ssl-cert \
    ufw \
    unzip \
    wget \
 && rm -rf /var/lib/apt/lists/*

# Configure mysql

RUN sed -i -e"s/^bind-address\s*=\s*127.0.0.1/bind-address = 0.0.0.0/" /etc/mysql/my.cnf

RUN service mysql start && \
    mysql -uroot -e "CREATE DATABASE IF NOT EXISTS lychee;" && \
    mysql -uroot -e "CREATE USER 'lychee'@'localhost' IDENTIFIED BY 'lychee';" && \
    mysql -uroot -e "GRANT ALL PRIVILEGES ON *.* TO 'lychee'@'localhost' WITH GRANT OPTION;" && \
    mysql -uroot -e "FLUSH PRIVILEGES;"

RUN mkdir /var/lib/mysql_init && \
    mv /var/lib/mysql/* /var/lib/mysql_init

# Configure php-fpm

RUN sed -i -e "s/upload_max_filesize\s*=\s*2M/upload_max_filesize = 1G/g" /etc/php5/fpm/php.ini
RUN sed -i -e "s/post_max_size\s*=\s*8M/post_max_size = 1G/g" /etc/php5/fpm/php.ini

RUN sed -i -e "s/memory_limit\s*=\s*128M/memory_limit = 256M/g" /etc/php5/fpm/php.ini
RUN sed -i -e "s/max_execution_time\s*=\s*30/max_execution_time = 300/g" /etc/php5/fpm/php.ini

RUN sed -i -e "s/output_buffering\s*=\s*4096/output_buffering = Off/g" /etc/php5/fpm/php.ini
RUN sed -i -e "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g" /etc/php5/fpm/php.ini
RUN sed -i -e "s:;\s*session.save_path\s*=\s*\"N;/path\":session.save_path = /tmp:g" /etc/php5/fpm/php.ini
RUN sed -i 's/;daemonize = yes/daemonize = no/g' /etc/php5/fpm/php-fpm.conf
RUN chown -R www-data:www-data /tmp

RUN php5enmod mcrypt

# Configure nginx

RUN mkdir /var/www
RUN chown www-data:www-data /var/www
RUN rm /etc/nginx/sites-enabled/*
RUN rm /etc/nginx/sites-available/*

RUN sed -i -e"s/keepalive_timeout\s*65/keepalive_timeout 2/" /etc/nginx/nginx.conf
RUN sed -i -e"s/keepalive_timeout 2/keepalive_timeout 2;\n\tclient_max_body_size 100m/" /etc/nginx/nginx.conf

RUN echo "daemon off;" >> /etc/nginx/nginx.conf
ADD conf/php.conf /etc/nginx/
ADD conf/lychee /etc/nginx/sites-enabled/

# Install Lychee

WORKDIR /var/www
RUN git clone https://github.com/electerious/Lychee.git lychee
RUN chown -R www-data:www-data /var/www/lychee
RUN chmod -R 770 /var/www/lychee
RUN chmod -R 777 /var/www/lychee/uploads/ 
RUN chmod -R 777 /var/www/lychee/data/

# Expose volumes

WORKDIR /
RUN ln -s /var/www/lychee/uploads uploads 
RUN ln -s /var/www/lychee/data data
RUN ln -s /var/lib/mysql mysql

VOLUME /uploads
VOLUME /data
VOLUME /mysql

# Expose ports

EXPOSE 80

# Setup supervisord

ADD conf/startup.conf /etc/supervisor/conf.d/
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]
