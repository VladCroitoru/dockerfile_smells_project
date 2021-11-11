FROM alpine:3.3
MAINTAINER Joerg Henning <henning.joerg@gmail.com>

ENV version=1

RUN apk update \
  && apk add nginx php-fpm

COPY nginx.conf /etc/nginx/nginx.conf
COPY php-fpm.conf /etc/php/php-fpm.conf
COPY run.sh /usr/bin/
COPY ["index.php", "favicon.ico", "/src/public/"]

EXPOSE 80
VOLUME ["/cache", "/tmp"]

CMD ["/usr/bin/run.sh"]
