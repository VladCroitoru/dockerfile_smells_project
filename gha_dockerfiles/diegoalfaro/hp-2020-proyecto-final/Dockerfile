FROM docker.io/bitnami/laravel:8
USER root
RUN apt update && apt install -y php-pgsql
USER bitnami
COPY . /app
COPY ./php.ini /opt/bitnami/php/etc/conf.d
WORKDIR /app
EXPOSE 3000
ENTRYPOINT [ "/app/entrypoint.sh" ]
CMD [ "php", "artisan", "serve", "--host=0.0.0.0", "--port=3000" ]