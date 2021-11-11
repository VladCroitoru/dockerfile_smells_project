FROM invartam/docker-alpine-php-fpm-advanced

COPY src /app

RUN apk --no-cache add nodejs wget git \
    && rm -rf /app/.git /app/.gitignore /app/*.md \
    && cd /app/ \
    && wget https://getcomposer.org/composer.phar \
    && php composer.phar install \
    && rm composer.phar \
    && cp .env.example .env \
    && chown -R www-data:www-data /app \
    && php artisan vendor:publish \
    && php artisan key:generate \    
    && npm install \
    && npm run dev \
    && apk del nodejs wget git

COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80
