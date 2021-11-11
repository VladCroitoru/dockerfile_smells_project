FROM alpine:edge
MAINTAINER bytepark GmbH <code@bytepark.de>

#RUN mkdir -p /usr/local/etc/php && ln -s /usr/local/etc/php /etc/php7

RUN apk upgrade -U && \
    apk --update --repository=http://dl-4.alpinelinux.org/alpine/edge/main add \
    libressl2.5-libcrypto libressl2.5-libssl musl curl bash git

# Add PHP 7
RUN apk upgrade -U && \
    apk --update --repository=http://dl-4.alpinelinux.org/alpine/edge/community add \
    shadow \
    php7-fpm \
    php7-ctype \
    php7-curl \
    php7-mcrypt \
    php7-fileinfo \
    php7-gd \
    php7-json \
    php7-ldap \
    php7-mbstring \
    php7-mcrypt \
    php7-mysqli \
    php7-opcache \
    php7-openssl \
    php7-pdo_mysql \
    php7-phar \
    php7-session \
    php7-simplexml \
    php7-tokenizer \
    php7-xml \
    php7-xmlwriter \
    php7-xsl \
    php7-zlib

# add PHP7 testing
RUN apk upgrade -U && \
    apk --update --repository=http://dl-4.alpinelinux.org/alpine/edge/testing add \
    php7-ssh2

#COPY /rootfs /

RUN mkdir -p /var/log/php-fpm && \
    touch /var/log/php-fpm/fpm-error.log

# cleanup
RUN rm -fr /var/cache/apk/*

EXPOSE 9000

COPY entrypoint.sh /usr/local/bin/entrypoint.sh
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

CMD [ "/usr/sbin/php-fpm7", "-F" ]
