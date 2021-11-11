FROM alpine:3.6
MAINTAINER Jordan Jones <jordancjones@gmail.com>

RUN apk --update add \
  nginx \
  php7-fpm \
  php7-pdo \
  php7-json \
  php7-openssl \
  php7-pgsql \
  php7-pdo_pgsql \
  php7-mcrypt \
  php7-sqlite3 \
  php7-pdo_sqlite \
  php7-ctype \
  php7-zlib \
  php7-xml \
  php7-gd \
  curl \
  py-pip \
  php7-curl \
  php7-zip \
  php7-iconv \
  php7-session \
  php7-tokenizer \
  supervisor

# Configure supervisor
RUN pip install --upgrade pip && \
    pip install supervisor-stdout

RUN mkdir -p /etc/nginx
RUN mkdir -p /run/nginx
RUN mkdir -p /var/run/php-fpm
RUN mkdir -p /var/log/supervisor

RUN rm /etc/nginx/nginx.conf
ADD nginx.conf /etc/nginx/nginx.conf

RUN rm /etc/php7/php-fpm.d/www.conf
ADD www.conf /etc/php7/php-fpm.d/www.conf

VOLUME ["/var/www", "/etc/nginx/sites-enabled"]

ADD nginx-supervisor.ini /etc/supervisor.d/nginx-supervisor.ini
ENV TIMEZONE America/Los_Angeles

RUN ln -sf /dev/stderr /var/log/nginx/error.log
RUN ln -sf /dev/stdout /var/log/nginx/access.log

EXPOSE 80 9000

CMD ["/usr/bin/supervisord"]
