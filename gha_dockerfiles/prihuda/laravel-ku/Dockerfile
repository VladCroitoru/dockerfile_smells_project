FROM marcusmyers/laravel
#FROM nginx
#HEALTHCHECK CMD curl -f http://localhost:8000/status || exit 1
#STOPSIGNAL SIGKILL

EXPOSE 80
EXPOSE 8000

COPY . /usr/share/nginx/html;
WORKDIR /usr/share/nginx/html;
RUN composer install
RUN cp .env.example .env
RUN php artisan key:generate
CMD [ "php", "artisan", "serve", "--host=0.0.0.0" ]
