FROM invartam/docker-alpine-php-fpm-advanced

RUN apk update \
    && apk add git \
    && git clone https://github.com/mybb/mybb2.git /app \
    && apk del git \
    && rm -rf /app/.git /app/.gitignore /app/*.md \
    && cd /app \
    && wget http://getcomposer.org/composer.phar \
    && php composer.phar install \
    && chown -R www-data:www-data /app

COPY nginx.conf /etc/nginx/nginx.conf
COPY start.sh /bin/start.sh
RUN chmod a+x /bin/start.sh

CMD ["/bin/start.sh"]

EXPOSE 80

# Folders to mount in rw :
#   - /logs
#   - /app/storage
