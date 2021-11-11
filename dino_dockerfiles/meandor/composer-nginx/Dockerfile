FROM ubuntu:latest
RUN apt-get update && \
    apt-get -y dist-upgrade -y && \
    apt-get -y autoremove && \
    apt-get -y install php7.0 php7.0-cli php7.0-mcrypt php7.0-mysql nginx curl openssl wget git php7.0-curl php7.0-xml php7.0-intl php7.0-gd php7.0-mbstring php7.0-fpm ssl-cert unzip zip && \
    rm -rf /var/lib/apt/lists/*
RUN chown -R www-data:www-data /var/lib/nginx
RUN chown -R www-data:www-data /var/www && chmod -R 0755 /var/www

COPY ./dist/php.ini /etc/php/7.0/fpm/php.ini
RUN service php7.0-fpm start
COPY ./dist/nginx.conf /etc/nginx/nginx.conf
COPY ./dist/default /etc/nginx/sites-available/default
COPY ./dist/install-composer.sh .
RUN ./install-composer.sh
RUN rm -rf /var/www/html/index.nginx-debian.html

CMD service php7.0-fpm start && nginx

EXPOSE 80
EXPOSE 443
