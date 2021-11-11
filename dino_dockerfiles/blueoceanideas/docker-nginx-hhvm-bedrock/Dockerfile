FROM ubuntu:xenial

# Originally based on https://github.com/philipz/docker-nginx-hhvm-wordpress
MAINTAINER Adam Yeats <ay@xadamy.xyz>

# Get latest version of software-properties-common first
RUN apt-get update && apt-get -y upgrade && apt-get -y install software-properties-common build-essential

# Pre-add nginx repo
RUN echo "deb http://ppa.launchpad.net/nginx/stable/ubuntu xenial main" > /etc/apt/sources.list.d/nginx-$nginx-xenial.list
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C300EE8C

# Pre-add nginx repo
RUN apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0x5a16e7281be7a449
RUN add-apt-repository "deb http://dl.hhvm.com/ubuntu $(lsb_release -sc) main"

# Pre-add php repo
RUN LC_ALL=C.UTF-8 add-apt-repository -y ppa:ondrej/php && apt-get -y update

# If it's not going to change often do it first to allow Docker build to
# use as much caching as possible to minimize build times
RUN apt-get update && apt-get -y upgrade

# Basic Requirements
RUN apt-get -y install nginx git curl unzip wget python-pip

# PHP
RUN apt-get -y install php7.1 php7.1-cli php7.1-common php7.1-curl php7.1-dev php7.1-fpm php7.1-gd php7.1-mbstring php7.1-mcrypt php7.1-mysql php7.1-opcache php7.1-xml php7.1-xmlrpc php7.1-zip php-redis

# Wordpress Requirements
RUN apt-get -y install libnuma-dev

# HHVM install
RUN apt-get -y install hhvm

WORKDIR /

# hhvm config
RUN /usr/share/hhvm/install_fastcgi.sh
RUN /etc/init.d/hhvm restart
RUN update-rc.d hhvm defaults
RUN /usr/bin/update-alternatives --install /usr/bin/php php /usr/bin/hhvm 60

# install Composer
RUN curl -sS https://getcomposer.org/installer | php
RUN chmod +x composer.phar
RUN mv composer.phar /usr/local/bin/composer

# install WP-CLI
RUN curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar
RUN chmod +x wp-cli.phar
RUN mv wp-cli.phar /usr/local/bin/wp

# some misc cleanup
WORKDIR /
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN rm /etc/nginx/sites-enabled/default

# Map local files
ADD nginx/bedrock /etc/nginx/sites-enabled/bedrock

# install ngxtop, useful for debugging
RUN pip install ngxtop

# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log && ln -sf /dev/stderr /var/log/nginx/error.log && ln -sf /dev/stderr /var/log/hhvm/error.log
RUN sed -i "/# server_name_in_redirect off;/ a\fastcgi_cache_path /var/run/nginx levels=1:2 keys_zone=drm_custom_cache:16m max_size=1024m inactive=60m;" /etc/nginx/nginx.conf

COPY docker-entrypoint.sh /entrypoint.sh
COPY makedb.php /makedb.php

ENTRYPOINT ["/entrypoint.sh"]
CMD ["nginx", "-g", "daemon off;"]
