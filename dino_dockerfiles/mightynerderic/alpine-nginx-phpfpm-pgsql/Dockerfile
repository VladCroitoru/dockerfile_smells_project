FROM alpine:3.8
MAINTAINER Eric Ball <eball@ccctechcenter.org>

RUN rm -rf /var/cache/apk/* && \
    rm -rf /tmp/* && \
    mkdir /run/nginx

RUN apk update

RUN apk --update --no-cache add \
  nginx \
  php7 \
  php7-ctype \
  php7-curl \
  php7-dom \
  php7-fileinfo \
  php7-fpm \
  php7-gd \
  php7-iconv \
  php7-json \
  php7-mbstring \
  php7-openssl \
  php7-pdo \
  php7-pdo_mysql \
  php7-pdo_pgsql \
  php7-pdo_sqlite \
  php7-pgsql \
  php7-session \
  php7-simplexml \
  php7-sqlite3 \
  php7-tokenizer \
  php7-xml \
  php7-xmlwriter \
  php7-zip \
  php7-zlib \
  curl \
  py-pip \
  supervisor

RUN apk add --no-cache --repository http://dl-cdn.alpinelinux.org/alpine/edge/community gnu-libiconv

ADD     build_pdftk.sh /bin/
ENV     VER_PDFTK=2.02

RUN apk --no-cache add --update unzip wget make fastjar gcc gcc-java g++ && \
  /bin/build_pdftk.sh && \
  apk del build-base unzip wget make fastjar && \
  rm -rf /var/cache/apk/* && \
  pdftk

# Configure supervisor
RUN pip install --upgrade pip && \
    pip install supervisor-stdout

RUN mkdir -p {/etc/nginx,/run/nginx,/var/run/php7-fpm,/var/log/supervisor}

RUN rm -f /etc/nginx/nginx.conf
ADD nginx.conf /etc/nginx/nginx.conf

RUN rm -f /etc/php7/php-fpm.conf
ADD php-fpm.conf /etc/php7/php-fpm.conf

RUN rm -f /etc/php7/php.ini
ADD php.ini /etc/php7/php.ini

VOLUME ["/var/www", "/etc/nginx/sites-enabled"]

ADD nginx-supervisor.ini /etc/supervisor.d/nginx-supervisor.ini
ENV TIMEZONE America/Los_Angeles

RUN ln -sf /dev/stderr /var/log/nginx/error.log
RUN ln -sf /dev/stdout /var/log/nginx/access.log

EXPOSE 80 9000

CMD ["/usr/bin/supervisord"]
