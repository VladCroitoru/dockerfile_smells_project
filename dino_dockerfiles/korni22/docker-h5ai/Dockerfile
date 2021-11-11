FROM alpine:latest

ENV H5AI_VERSION 0.29.2

RUN apk -U add \
    nginx \
    supervisor \
    tini \
    php7-fpm \
    php7-curl \
    php7-iconv \
    php7-xml \
    php7-dom \
    php7-json \
    php7-zlib \
    php7-session \
    wget \
    unzip \
    patch \
  && mkdir -p /var/www \
  && wget "http://release.larsjung.de/h5ai/h5ai-$H5AI_VERSION.zip" \
  && mkdir -p /usr/share/h5ai \
  && unzip "h5ai-$H5AI_VERSION.zip" -d /usr/share/h5ai
COPY class-setup.php.patch class-setup.php.patch
RUN patch -p1 -u -d /usr/share/h5ai/_h5ai/private/php/core/ -i /class-setup.php.patch && rm class-setup.php.patch

COPY nginx.conf /etc/nginx/nginx.conf
COPY supervisord.conf /etc/supervisor/supervisord.conf
COPY startup /usr/local/bin/startup

RUN chmod +x /usr/local/bin/startup
EXPOSE 80
VOLUME [ "/var/www" ]
CMD ["/sbin/tini","--","startup"]
