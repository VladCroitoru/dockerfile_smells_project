FROM nimmis/alpine-glibc

MAINTAINER fadlihub <fadli.ramadhan@elitery.com>

COPY root/. /

RUN apk update && apk upgrade && \
    cd /root && \
    curl https://download-cdn.resilio.com/stable/linux-x64/resilio-sync_x64.tar.gz | tar xfz - && \
    mv rslsync /usr/local/bin/btsync && \
    rm -rf /var/cache/apk/* && mkdir -p /var/www/html/wp-content && adduser -S www-data && addgroup -S www-data && chown -R www-data:www-data /var/www/html

VOLUME /var/www/html


