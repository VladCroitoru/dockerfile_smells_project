FROM richarvey/nginx-php-fpm
MAINTAINER Alexis Pereda <alexis@pereda.fr>

ENV UID 1000
ENV GID 1000

RUN echo 'http://dl-cdn.alpinelinux.org/alpine/v3.5/community' >> /etc/apk/repositories
RUN apk update && apk add --no-cache shadow

COPY prestart.sh /prestart.sh

VOLUME /var/www/html

EXPOSE 443 80

CMD ["/prestart.sh"]
