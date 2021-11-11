# Use phusion/baseimage as base image. To make your builds reproducible, make
# sure you lock down to a specific version, not to `latest`!
# See https://github.com/phusion/baseimage-docker/blob/master/Changelog.md for
# a list of version numbers.
FROM phusion/baseimage:latest
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

WORKDIR /tmp



# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

RUN DEBIAN_FRONTEND=noninteractive add-apt-repository -y ppa:nginx/stable
RUN DEBIAN_FRONTEND=noninteractive add-apt-repository ppa:ondrej/php
RUN echo "deb http://archive.ubuntu.com/ubuntu/ trusty-backports main restricted" >> /etc/apt/sources.list
RUN echo "deb-src http://archive.ubuntu.com/ubuntu/ trusty-backports main restricted" >> /etc/apt/sources.list

RUN DEBIAN_FRONTEND=noninteractive apt-get -qy update && apt-get -qy upgrade && locale-gen en_US.UTF-8 && export LANG=en_US.UTF-8
RUN DEBIAN_FRONTEND=noninteractive apt-get -qy install curl nginx git zip re2c libhiredis-dev --fix-missing
RUN DEBIAN_FRONTEND=noninteractive apt-get -qy install build-essential --fix-missing


# install nginx and php7 and phpredis
RUN DEBIAN_FRONTEND=noninteractive apt-get -qy --force-yes install php7.0-fpm php7.0-curl php7.0-cli php7.0-common php7.0-json php7.0-opcache  php7.0-mysql php7.0-phpdbg php7.0-gd php7.0-imap php7.0-ldap php7.0-pgsql php7.0-pspell php7.0-recode php7.0-snmp php7.0-tidy php7.0-dev php7.0-intl php7.0-gd



# install phpredis
RUN git clone https://github.com/phpredis/phpredis.git  \
    && cd phpredis \
    && git checkout php7 \
    && phpize && ./configure \
    && make \
    && make install

RUN echo "extension=redis.so" > /etc/php/7.0/mods-available/redis.ini
RUN ln -sf /etc/php/7.0/mods-available/redis.ini /etc/php/7.0/fpm/conf.d/20-redis.ini
RUN ln -sf /etc/php/7.0/mods-available/redis.ini /etc/php/7.0/cli/conf.d/20-redis.ini



# install phpiredis
RUN git clone https://github.com/Danack/phpiredis.git  \
    && cd phpiredis \
    && phpize && ./configure --enable-phpiredis \
    && make \
    && make install

RUN echo "extension=phpiredis.so" > /etc/php/7.0/mods-available/phpiredis.ini
RUN ln -sf /etc/php/7.0/mods-available/phpiredis.ini /etc/php/7.0/fpm/conf.d/20-phpiredis.ini
RUN ln -sf /etc/php/7.0/mods-available/phpiredis.ini /etc/php/7.0/cli/conf.d/20-phpiredis.ini


RUN ls -lR /etc/php/

#nginx configuration
ADD  ./config-nginx/cg_site_available.conf /etc/nginx/sites-available/
RUN mv /etc/nginx/sites-available/cg_site_available.conf /etc/nginx/sites-available/default

#http://nls.io/optimize-nginx-and-php-fpm-max_children/
ADD ./config-nginx/nginx.conf /etc/nginx/nginx.conf

#nginx configuration
ADD  ./config-nginx/cg_site_available.conf /etc/nginx/sites-available/
RUN mv /etc/nginx/sites-available/cg_site_available.conf /etc/nginx/sites-available/default

#php fpm configuration
ADD ./config-nginx/www.conf /etc/php/7.0/fpm/pool.d/www.conf
RUN echo "cgi.fix_pathinfo = 0;" >> /etc/php/7.0/fpm/php.ini




#main service
RUN mkdir /etc/service/nginx-fpm-opcache && \
    echo "#!/bin/bash" >> /run.sh && \
    echo "service php7.0-fpm start" >> /run.sh && \
    echo "/usr/sbin/nginx" >> /run.sh && chmod +x /run.sh && \
    mv /run.sh /etc/service/nginx-fpm-opcache/run


#main docker-squash script
RUN touch /usr/local/bin/docker-squash-script && \
        echo "#!/bin/bash" >> /run.sh && \
        echo "apt-get purge php5-common autoremove build-essential -y" >> /run.sh && \
        echo "apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*" >> /run.sh && \
        chmod +x /usr/local/bin/docker-squash-script



expose 80


#ENTRYPOINT ["/sbin/my_init"]
