FROM alastairhm/alpine-lighttpd-php:latest
MAINTAINER Alastair Montgomery <alastair@montgomery.me.uk>

ADD lighttpd.conf /etc/lighttpd/lighttpd.conf

RUN wget http://download.dokuwiki.org/src/dokuwiki/dokuwiki-stable.tgz -O dokuwiki.tgz && \
    tar zxf dokuwiki.tgz && \
    mkdir -p /var/doku && \
    mv dokuwiki-*/* /var/doku && \
    rm -rf dokuwiki* && \
    chown -R www-data. /var/doku

RUN mkdir -p /storage && \
    cp -R /var/doku/data /storage && \
    cp -R /var/doku/conf /storage

EXPOSE 80

VOLUME ["/var/doku/data","/var/doku/conf"]

ADD start.sh /start.sh
ENTRYPOINT /start.sh


