FROM alpine:3.3
MAINTAINER Alastair Montgomery <alastair@montgomery.me.uk>

RUN apk --update add \
    lighttpd \
    php-common \
    php-iconv \
    php-json \
    php-gd \
    php-curl \
    php-xml \
    php-pgsql \
    php-imap \
    php-cgi \
    fcgi \
    php-pdo \
    php-pdo_pgsql \
    php-soap \
    php-xmlrpc \
    php-posix \
    php-mcrypt \
    php-gettext \
    php-ldap \
    php-ctype \
    php-dom \
    php-fpm \
    php-mysqli \
    imagemagick \
    wget \
    unzip && \
    rm -rf /var/cache/apk/*

ADD lighttpd.conf /etc/lighttpd/lighttpd.conf
RUN adduser www-data -G www-data -H -s /bin/false -D
RUN mkdir -p /run/lighttpd/                                                                                                                                                       
RUN chown www-data. /run/lighttpd/

RUN wget -q -O piwigo.zip http://piwigo.org/download/dlcounter.php?code=latest && \
    unzip -q piwigo.zip && \
    mv piwigo/* /var/www/ && \
    chown -R www-data. /var/www && \
    rm -r piwigo*

RUN mkdir /template
RUN mv /var/www/galleries /template/
RUN mv /var/www/themes /template/
RUN mv /var/www/plugins /template/
RUN mv /var/www/local /template/

EXPOSE 80

VOLUME ["/var/www/galleries", "/var/www/themes", "/var/www/plugins", "/var/www/local", "/var/www/_data/i"]

ADD start.sh /start.sh
ENTRYPOINT /start.sh

