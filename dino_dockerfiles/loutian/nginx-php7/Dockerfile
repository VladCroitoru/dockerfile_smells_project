FROM centos
MAINTAINER loutian <loutian@gmail.com>
##
# Nginx: 1.9.14
# PHP  : 7.0.5
##
#Install system library
#RUN yum update -y

ENV PHP_VERSION 7.0.5
ENV NGINX_VERSION 1.9.14

RUN yum install -y gcc \
    gcc-c++ \
    autoconf \
    automake \
    libtool \
    zip \
    unzip \
    make \
    cmake && \
    yum clean all

#Install PHP library
## libmcrypt-devel DIY
RUN rpm -ivh http://dl.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm && \
    yum install -y wget \
    zlib \
    zlib-devel \
    openssl \
    openssl-devel \
    pcre-devel \
    libxml2 \
    libxml2-devel \
    libcurl \
    libcurl-devel \
    libpng-devel \
    libjpeg-devel \
    freetype-devel \
    libmcrypt-devel \
    openssh-server \
    python-setuptools && \
    yum clean all

#Add user
RUN groupadd -r www && \
    useradd -M -s /sbin/nologin -r -g www www

#Download nginx & php
RUN mkdir -p /home/nginx-php && cd $_ && \
    wget -c -O nginx.tar.gz http://nginx.org/download/nginx-$NGINX_VERSION.tar.gz && \
    wget -O php.tar.gz http://php.net/distributions/php-$PHP_VERSION.tar.gz && \
    curl -O -SL https://github.com/xdebug/xdebug/archive/XDEBUG_2_4_0RC3.tar.gz

#Make install nginx
RUN cd /home/nginx-php && \
    tar -zxvf nginx.tar.gz && \
    cd nginx-$NGINX_VERSION && \
    ./configure --prefix=/usr/local/nginx \
    --user=www --group=www \
    --error-log-path=/var/log/nginx_error.log \
    --http-log-path=/var/log/nginx_access.log \
    --pid-path=/var/run/nginx.pid \
    --with-pcre \
    --with-http_ssl_module \
    --with-http_v2_module \
    --without-mail_pop3_module \
    --without-mail_imap_module \
    --with-http_gzip_static_module && \
    make -j8 && make install

#Make install php
RUN cd /home/nginx-php && \
    tar zvxf php.tar.gz && \
    cd php-$PHP_VERSION && \
    ./configure --prefix=/usr/local/php \
    --with-config-file-path=/usr/local/php/etc \
    --with-config-file-scan-dir=/usr/local/php/etc/php.d \
    --with-fpm-user=www \
    --with-fpm-group=www \
    --with-mcrypt=/usr/include \
    --with-mysqli \
    --with-pdo-mysql \
    --with-openssl \
    --with-gd \
    --with-iconv \
    --with-zlib \
    --with-gettext \
    --with-curl \
    --with-png-dir \
    --with-jpeg-dir \
    --with-freetype-dir \
    --with-xmlrpc \
    --with-mhash \
    --enable-fpm \
    --enable-xml \
    --enable-shmop \
    --enable-sysvsem \
    --enable-inline-optimization \
    --enable-mbregex \
    --enable-mbstring \
    --enable-ftp \
    --enable-gd-native-ttf \
    --enable-mysqlnd \
    --enable-pcntl \
    --enable-sockets \
    --enable-zip \
    --enable-soap \
    --enable-session \
    --enable-opcache \
    --enable-bcmath \
    --enable-exif \
    --enable-fileinfo \
    --disable-rpath \
    --enable-ipv6 \
    --disable-debug \
    --without-pear && \
    make -j8 && make install

#Add xdebug extension
RUN cd /home/nginx-php && \
    tar -zxvf XDEBUG_2_4_0RC3.tar.gz && \
    cd xdebug-XDEBUG_2_4_0RC3 && \
    /usr/local/php/bin/phpize && \
    ./configure --enable-xdebug --with-php-config=/usr/local/php/bin/php-config && \
    make -j8 && \
    cp modules/xdebug.so /usr/local/php/lib/php/extensions/xdebug.so

RUN	cd /home/nginx-php/php-$PHP_VERSION && \
    cp php.ini-production /usr/local/php/etc/php.ini && \
    cp /usr/local/php/etc/php-fpm.conf.default /usr/local/php/etc/php-fpm.conf && \
    cp /usr/local/php/etc/php-fpm.d/www.conf.default /usr/local/php/etc/php-fpm.d/www.conf

#Install supervisor
RUN easy_install supervisor && \
    mkdir -p /var/log/supervisor && \
    mkdir -p /var/run/sshd && \
    mkdir -p /var/run/supervisord


#Add php-redis
COPY package/redis-php7.zip /tmp/
WORKDIR /tmp/
RUN unzip redis-php7.zip
WORKDIR /tmp/phpredis-php7 
RUN /usr/local/php/bin/phpize
RUN ./configure --with-php-config=/usr/local/php/bin/php-config
RUN make -j8 && make install


#add yaf
COPY package/yaf-php7.zip /tmp/
WORKDIR /tmp/
RUN unzip yaf-php7.zip
WORKDIR /tmp/yaf-php7/
RUN /usr/local/php/bin/phpize
RUN ./configure --with-php-config=/usr/local/php/bin/php-config
RUN make -j8 && make install

RUN echo "extension=redis.so" >> /usr/local/php/etc/php.ini
RUN echo "extension=yaf.so" >> /usr/local/php/etc/php.ini
RUN rm -rf /tmp/*

WORKDIR /root/

#Add supervisord conf
ADD config/supervisord.conf /etc/supervisord.conf

#Remove zips
RUN cd / && rm -rf /home/nginx-php

#Create web folder
VOLUME ["/data/www", "/usr/local/nginx/conf/ssl", "/usr/local/nginx/conf/vhost", "/usr/local/php/etc/php.d"]
ADD index.php /data/www/index.php

ADD config/xdebug.ini /usr/local/php/etc/php.d/xdebug.ini

#Update nginx config
ADD config/nginx.conf /usr/local/nginx/conf/nginx.conf

#change chown
RUN chown -R www. /data/www/

#Start
ADD start.sh /start.sh
RUN chmod +x /start.sh

#Set port
EXPOSE 80 443 9000

#Start it
ENTRYPOINT ["/start.sh"]

