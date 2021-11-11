FROM fauria/lamp

ENV LOG_STDOUT true
ENV LOG_STDERR true
ENV LOG_LEVEL debug

RUN mkdir tmpredis && apt-get install -y php7.0-dev wget unzip && cd tmpredis && wget https://github.com/phpredis/phpredis/archive/php7.zip -O phpredis.zip \
    && unzip -o /tmpredis/phpredis.zip && mv /tmpredis/phpredis-* /tmpredis/phpredis && cd /tmpredis/phpredis && phpize && ./configure && make && make install \
    && touch /etc/php/7.0/mods-available/redis.ini && echo extension=redis.so > /etc/php/7.0/mods-available/redis.ini \
    && ln -s /etc/php/7.0/mods-available/redis.ini /etc/php/7.0/apache2/conf.d/redis.ini \
    && ln -s /etc/php/7.0/mods-available/redis.ini /etc/php/7.0/fpm/conf.d/redis.ini \
    && ln -s /etc/php/7.0/mods-available/redis.ini /etc/php/7.0/cli/conf.d/redis.ini

RUN rm /var/www/html/index.html -f
COPY conf/000-default.conf /etc/apache2/sites-available/000-default.conf
COPY src/ /var/www/html/
