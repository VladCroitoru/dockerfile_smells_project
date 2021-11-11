FROM hobord/alpine-ngnix-php7-fpm-devenv
MAINTAINER Balazs Szabo <balazs.szabo@gmail.com>
ADD files/nginx.conf /etc/nginx/

RUN ln -s /usr/bin/php7 /usr/bin/php
RUN  curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer 2>/dev/null 1>/dev/null


VOLUME ["/DATA","/DATA/htdocs"]
