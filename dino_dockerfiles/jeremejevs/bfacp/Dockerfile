FROM alpine:edge

RUN \
  echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >> \
    /etc/apk/repositories && \
  apk update && \
  apk add \
    nginx \
    php5-fpm \
    php5-mcrypt \
    php5-openssl \
    php5-pdo \
    php5-pcntl \
    php5-curl \
    php5-posix \
    php5-pdo_mysql \
    php5-ctype \
    composer

WORKDIR /app
RUN composer create-project --prefer-dist --no-scripts --keep-vcs \
  adkgamers/bfadmincp .
COPY .env.php ./

COPY nginx.conf /etc/nginx/
RUN sed -ie 's/127\.0\.0\.1:9000/\/var\/run\/php5-fpm\.sock/g' \
  /etc/php5/php-fpm.conf
RUN sed -ie 's/;clear_env/clear_env/g' /etc/php5/php-fpm.conf

EXPOSE 80
CMD php-fpm && nginx
