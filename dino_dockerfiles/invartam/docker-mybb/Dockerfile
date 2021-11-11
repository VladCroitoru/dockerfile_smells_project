FROM invartam/docker-alpine-php-fpm-advanced

RUN apk update \
    && apk add git \
    && git clone https://github.com/mybb/mybb.git /app \
    && rm -rf /app/.git /app/.gitignore /app/*.md \
    && apk del git \
    && chown -R www-data:www-data /app

EXPOSE 80

# Folders to mount in rw :
#   - /logs
#   - /app/inc/config.php
#   - /app/inc/settings.php
#   - /app/uploads
