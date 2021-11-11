FROM debian:jessie

# Add nginx PPA key
RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys 573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62
RUN echo "deb http://nginx.org/packages/mainline/debian/ jessie nginx" >> /etc/apt/sources.list

ENV NGINX_VERSION 1.9.0-1~jessie
ENV PHP_VERSION 5.6.7+dfsg-1

# Install required packages
RUN apt-get update && \
    apt-get install -y ca-certificates nginx=${NGINX_VERSION} curl git \
    php5-fpm=${PHP_VERSION} php5-curl supervisor && \
    rm -rf /var/lib/apt/lists/*

# Install composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# Add compose config and install dependencies
ADD composer.lock composer.json /var/www/
WORKDIR /var/www/
RUN /usr/local/bin/composer install --prefer-source --no-interaction

ADD index.php /var/www/

ADD docker/nginx.conf /etc/nginx/conf.d/default.conf
ADD docker/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

RUN sed -i -e "s/user  nginx;/user  www-data;/g" /etc/nginx/nginx.conf

RUN sed -i -e "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g" /etc/php5/fpm/php.ini
RUN sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php5/fpm/php-fpm.conf

# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log
RUN ln -sf /dev/stderr /var/log/nginx/error.log

EXPOSE 80

CMD ["/usr/bin/supervisord", "-n"]