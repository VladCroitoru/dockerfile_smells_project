FROM alpine:3.4
MAINTAINER Chris Batis <clbatis@taosnet.com>

RUN apk --update add apache2 apache2-ssl php5-apache2 curl \
    php5-json php5-phar php5-openssl php5-curl php5-mcrypt php5-ctype php5-gd php5-xml php5-dom php5-iconv php5-zip \
    && rm -f /var/cache/apk/* \
    && mkdir /run/apache2

EXPOSE 80 443
ENTRYPOINT ["/apache.sh"]
CMD ["-DFOREGROUND"]
COPY apache.sh /apache.sh
COPY httpd.conf /etc/apache2/httpd.conf
COPY site.conf /etc/apache2/site.conf
