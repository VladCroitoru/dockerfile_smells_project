FROM ubuntu:14.04
MAINTAINER Lixinghua <lixinghua2010@gmail.com>

# Install packages
ADD provision/provision.sh /provision.sh
ADD provision/serve.sh /serve.sh
ADD provision/run.sh /run.sh

RUN chmod +x /*.sh

RUN ./provision.sh

ADD . /var/www/html

RUN cd /var/www/html && composer install -v && chmod -R 777 storage && chmod -R 777 bootstrap/cache && curl https://raw.githubusercontent.com/laravel/laravel/master/.env.example -o .env && php artisan key:generate

EXPOSE 80 22 35729 9876
CMD ["/run.sh"]
