FROM ubuntu:latest

MAINTAINER Lee Yen <leeyenwork@gmail.com>

ENV TERM xterm

RUN apt-get -y update
RUN apt-get -y install nginx \
    php-gettext php-pear php-imagick \
    php7.0-curl php7.0-dev libgpgme11-dev libpcre3-dev \
    php7.0-fpm php7.0-gd php7.0-imap \
    php7.0-mcrypt php7.0-mysqlnd php7.0-sybase php7.0-mbstring \
    php7.0-intl php7.0-zip php7.0-soap \
    git nano wget supervisor curl pkg-config dialog

RUN pecl install mongodb

RUN curl -sL https://getcomposer.org/installer | php \
    && mv composer.phar /usr/local/bin/composer

# html to pdf
 RUN apt-get install -y gdebi
 RUN cd /tmp && \
    wget http://download.gna.org/wkhtmltopdf/0.12/0.12.2.1/wkhtmltox-0.12.2.1_linux-trusty-amd64.deb && \
    gdebi --n wkhtmltox-0.12.2.1_linux-trusty-amd64.deb
RUN apt-get -y install wkhtmltox xvfb fonts-wqy-microhei

RUN apt-get remove -y vim-common
RUN apt-get install -y vim

#RUN DEBIAN_FRONTEND=noninteractive apt-get install -y xorg

RUN echo 'LANG="en_US.UTF-8"' > /etc/default/locale && \
    echo 'LANG="zh_TW.UTF-8"' > /etc/default/locale && \
    echo 'LANG="zh_HK.UTF-8"' > /etc/default/locale && \
    echo 'LANG="zh_CN.UTF-8"' > /etc/default/locale && \
    echo 'LANG="th_TH.UTF-8"' > /etc/default/locale && \
    echo 'LANG="id_ID.UTF-8"' > /etc/default/locale && \
    echo 'LANG="ko_KR.UTF-8"' > /etc/default/locale && \
    echo 'LANG="ja_JP.UTF-8"' > /etc/default/locale && \
    locale-gen en_US.UTF-8 && \
    locale-gen zh_TW.UTF-8 && \
    locale-gen zh_CN.UTF-8 && \
    locale-gen zh_HK.UTF-8 && \
    locale-gen th_TH.UTF-8 && \
    locale-gen id_ID.UTF-8 && \
    locale-gen ko_KR.UTF-8 && \
    locale-gen ja_JP.UTF-8

RUN mkdir /run/php

COPY ./configs/supervisor/supervisord.conf /etc/supervisor/supervisord.conf
COPY ./configs/supervisor/conf.d/ /etc/supervisor/conf.d/
COPY ./configs/php/php.ini /etc/php/7.0/fpm/php.ini
COPY ./configs/php/php.ini /etc/php/7.0/cli/php.ini
COPY ./configs/php/pool.d/www.conf /etc/php/7.0/fpm/pool.d/www.conf

COPY ./configs/nginx/nginx.conf /etc/nginx/nginx.conf
COPY ./configs/nginx/sites-enabled/ /etc/nginx/sites-enabled/
COPY ./configs/nginx/conf.d/ /etc/nginx/conf.d/
RUN echo "extension=mongodb.so" >> /etc/php/7.0/cli/php.ini \
    && echo "extension=mongodb.so" >> /etc/php/7.0/fpm/php.ini

#RUN ln -sf /dev/stdout /var/log/nginx/access.log \
#    && ln -sf /dev/stderr /var/log/nginx/error.log

VOLUME ["/var/www/html", "/etc/nginx/conf.d", "/etc/nginx/sites-enabled"]
CMD ["/usr/bin/supervisord"]

EXPOSE 80