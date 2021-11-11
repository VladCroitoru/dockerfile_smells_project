FROM php:7.4-fpm-alpine

RUN apk add --no-cache nginx wget nodejs npm php7-pdo php7-pdo_mysql 

# Add and Enable PHP-PDO Extenstions
RUN docker-php-ext-install pdo pdo_mysql
#RUN docker-php-ext-enable pdo_mysql

# Remove Cache
RUN rm -rf /var/cache/apk/*

RUN mkdir -p /run/nginx

COPY docker/nginx.conf /etc/nginx/nginx.conf

COPY . /var/www/html

RUN chown -R www-data: /var/www/html

RUN sh -c "wget http://getcomposer.org/composer.phar && chmod a+x composer.phar && mv composer.phar /usr/local/bin/composer"
RUN cd /var/www/html && \
    /usr/local/bin/composer install --no-dev

#RUN npm shrinkwrap

RUN npm install

RUN npm run production
#RUN npm run dev

EXPOSE 80 443 8080

RUN chmod +rx /var/www/html/docker/startup.sh

CMD sh /var/www/html/docker/startup.sh