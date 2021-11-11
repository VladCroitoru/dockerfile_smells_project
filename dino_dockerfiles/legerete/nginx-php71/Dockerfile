FROM centos:7
MAINTAINER Petr Besir Horacek <petr@mondayfactory.cz>

ENV NGINX_VERSION 1.11.10
ENV PHP_VERSION 7.1.2

RUN yum install -y gcc \
    gcc-c++ \
    autoconf \
    automake \
    libtool \
    make \
    cronie \
    unzip \
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
    wget -O php7.zip https://github.com/phpredis/phpredis/archive/master.zip

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
    --without-mail_pop3_module \
    --without-mail_imap_module \
    --with-http_gzip_static_module && \
    make && make install

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
    --enable-calendar \
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
    --enable-cli \
    --without-pear && \
    make && make install && make test > /dev/null && \
    ln -s /usr/local/php/bin/php /usr/bin/php

#Add redis extension
RUN cd /home/nginx-php && \
	unzip php7.zip

RUN	cd /home/nginx-php/phpredis-master
RUN	/usr/local/php/bin/phpize
RUN	./configure --with-php-config=/usr/local/php/bin/php-config
RUN	make && make install
RUN	cp modules/redis.so /usr/local/php/lib/php/extensions/no-debug-non-zts-20160303/

RUN mkdir -p /usr/local/php/etc/php.d && chmod 0777 /usr/local/php/etc/php.d &&  echo 'extension=redis.so' > /usr/local/php/etc/php.d/redis.ini

ADD ./php-fpm.conf /usr/local/php/etc/php-fpm.conf
ADD ./www.conf /usr/local/php/etc/php-fpm.d/www.conf

ADD php.ini /usr/local/php/etc/php.ini

RUN ln -s /usr/local/php/bin/php /usr/bin/php

RUN curl -s http://getcomposer.org/installer | php && mv ./composer.phar /usr/local/bin/composer

#Install supervisor
RUN easy_install supervisor && \
    mkdir -p /var/log/supervisor && \
    mkdir -p /var/run/sshd && \
    mkdir -p /var/run/supervisord

#Add supervisord conf
ADD supervisord.conf /etc/supervisord.conf

#Remove zips
RUN cd / && rm -rf /home/nginx-php

#Create web folder
VOLUME ["/usr/local/nginx/conf/ssl", "/usr/local/nginx/conf/vhost", "/usr/local/php/etc/php.d"]
RUN mkdir -p /data/www && chown -R www:www /data/www
ADD index.php /data/www/index.php

#Update nginx config
ADD nginx.conf /usr/local/nginx/conf/nginx.conf

#Start
ADD start.sh ./start.sh
RUN chmod +x ./start.sh

#Set port
EXPOSE 80 443

WORKDIR /data

#Start it
ENTRYPOINT ["/start.sh"]
