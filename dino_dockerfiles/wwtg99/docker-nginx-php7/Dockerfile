FROM centos:7
MAINTAINER wwtg99 <wwtg99@126.com>

# Update yum repo
# RUN wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo

# Add dir & user
RUN mkdir -p /data/{www,ext,conf/{nginx,supervisord},log,script} && \
    useradd -r -s /sbin/nologin -d /data/www -M www && \
    chown -R www:www /data/www /data/log
WORKDIR /data/ext

# Install base library
RUN set -x && \
    yum install -y gcc \
    gcc-c++ \
    autoconf \
    automake \
    libtool \
    wget \
    make \
    cmake \
    epel-release && \

# Install library
    rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm && \
    rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm && \
    yum install -y zlib \
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
    postgresql-devel \
    git \
    python-setuptools \
    nginx \

# Install PHP
    php72w php72w-fpm php72w-cli php72w-common php72w-devel php72w-gd \
    php72w-pdo php72w-mysqlnd php72w-mysqli php72w-mbstring php72w-bcmath \
    php72w-fpm php72w-opcache php72w-pgsql php72w-process php72w-xml && \

# Install supervisor
    easy_install supervisor && \

# Install composer
    wget https://getcomposer.org/installer -O /data/ext/composer-setup.php && \
    php /data/ext/composer-setup.php && ln -s /data/ext/composer.phar /bin/composer && \

# Install PHP mongo
    wget https://pecl.php.net/get/mongodb-1.4.0.tgz -O /data/ext/mongodb-1.4.0.tgz && \
    tar zxf /data/ext/mongodb-1.4.0.tgz -C /data/ext
WORKDIR /data/ext/mongodb-1.4.0
RUN /usr/bin/phpize && \
    ./configure --with-php-config=/usr/bin/php-config && \
    make && make install && \
    echo "extension=mongodb.so" > /etc/php.d/mongodb.ini

# Clean OS
RUN yum clean all && \
    rm -rf /tmp/* /var/cache/{yum,ldconfig} /etc/my.cnf{,.d} && \
    mkdir -p --mode=0755 /var/cache/{yum,ldconfig} && \
    find /var/log -type f -delete && \
    rm -fr /data/ext/mongodb-1.4.0 /data/ext/mongodb-1.4.0.tgz /data/ext/composer-setup.php

# Add config file
COPY conf/nginx.conf /etc/nginx/nginx.conf
COPY conf/php-fpm.conf /etc/php-fpm.d/www.conf
COPY conf/supervisord.conf /etc/supervisord.conf

# Create volume
VOLUME ["/data/www", "/data/conf/nginx", "/data/conf/supervisord", "/data/log", "/data/script"]

# Add home page
WORKDIR /data/www
COPY index.php /data/www/

# Add scripts
COPY script.sh /data/script/
COPY start.sh /

# Set port
EXPOSE 80 443

# Start web server
CMD ["/bin/bash", "/start.sh"]
