FROM nginx

MAINTAINER Nam Khanh Do <donamkhanh@gmail.com>

ENV APP_MAGE_MODE default

RUN echo "deb http://packages.dotdeb.org jessie all" > /etc/apt/sources.list.d/dotdeb.list
COPY dotdeb.gpg /tmp/
RUN apt-key add /tmp/dotdeb.gpg
RUN apt-get update && apt-get install -y zip unzip git vim php7.0 php7.0-fpm php7.0-curl php7.0-gd php7.0-intl php7.0-json php7.0-pgsql php7.0-phpdbg php7.0-redis php7.0-mysql php7.0-cli php7.0-xml php7.0-mcrypt php7.0-mbstring php7.0-zip

RUN sed -i "s/user *nginx/user nginx www-data/g" /etc/nginx/nginx.conf
COPY nginx_conf/* /etc/nginx/conf.d/
COPY start.sh  /usr/local/bin/start.sh

RUN rm -rf /tmp/*

ADD https://getcomposer.org/composer.phar /usr/bin/composer
RUN chmod +x /usr/bin/composer

WORKDIR /usr/share/nginx/html/

EXPOSE 80 443

CMD ["/usr/local/bin/start.sh"]
