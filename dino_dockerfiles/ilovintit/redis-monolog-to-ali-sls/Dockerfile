FROM ilovintit/php71-apache-with-node
MAINTAINER ilovinti <ilovintit@gmail.com>

#部署代码
RUN mkdir -p /app
WORKDIR /app
COPY ./composer.json /app/
COPY ./composer.lock /app/
RUN composer install --prefer-dist  --no-autoloader --no-scripts
COPY . /app
RUN composer install --prefer-dist
RUN chown -R www-data:www-data /app

#配置supervisor

COPY ./supervisord.conf /etc/supervisor/conf.d/supervisord.conf

#CMD ["/usr/bin/supervisord"]
CMD ["/usr/local/bin/php","/app/sync.php"]