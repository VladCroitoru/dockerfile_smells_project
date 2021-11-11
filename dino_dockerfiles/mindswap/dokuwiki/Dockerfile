# DESCRIPTION:    Image with DokuWiki

FROM ubuntu:16.04
MAINTAINER MindSwap <mindswap@ro.ru>

RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get install -y \
    supervisor \
    nginx \
    php-fpm \
    php-gd \
    wget \
    unzip && \
    apt-get clean autoclean && \
    apt-get autoremove && \
    rm -rf /var/lib/{apt,dpkg,cache,log}
    
ENV DOKUWIKI_VERSION 2018-04-22a
ENV MD5_CHECKSUM 18765a29508f96f9882349a304bffc03

RUN mkdir -p /var/www /var/www/lib/plugins/ /var/dokuwiki-storage/data /var/run/php &&  \
    cd /var/www && \
    wget -q "http://download.dokuwiki.org/src/dokuwiki/dokuwiki-$DOKUWIKI_VERSION.tgz" && \
    echo "$MD5_CHECKSUM  dokuwiki-$DOKUWIKI_VERSION.tgz" | md5sum -c - && \
    tar xzf "dokuwiki-$DOKUWIKI_VERSION.tgz" --strip 1 && \
    rm "dokuwiki-$DOKUWIKI_VERSION.tgz" && \
    mv /var/www/data/pages /var/dokuwiki-storage/data/pages && \
    ln -s /var/dokuwiki-storage/data/pages /var/www/data/pages && \
    mv /var/www/data/meta /var/dokuwiki-storage/data/meta && \
    ln -s /var/dokuwiki-storage/data/meta /var/www/data/meta && \
    mv /var/www/data/media /var/dokuwiki-storage/data/media && \
    ln -s /var/dokuwiki-storage/data/media /var/www/data/media && \
    mv /var/www/data/media_attic /var/dokuwiki-storage/data/media_attic && \
    ln -s /var/dokuwiki-storage/data/media_attic /var/www/data/media_attic && \
    mv /var/www/data/media_meta /var/dokuwiki-storage/data/media_meta && \
    ln -s /var/dokuwiki-storage/data/media_meta /var/www/data/media_meta && \
    mv /var/www/data/attic /var/dokuwiki-storage/data/attic && \
    ln -s /var/dokuwiki-storage/data/attic /var/www/data/attic && \
    mv /var/www/conf /var/dokuwiki-storage/conf && \
    ln -s /var/dokuwiki-storage/conf /var/www/conf

RUN wget -q "https://github.com/selfthinker/dokuwiki_plugin_wrap/archive/stable.zip" && \
    unzip stable.zip -d /var/www/lib/plugins/ && \
    mv /var/www/lib/plugins/dokuwiki_plugin_wrap-stable/ /var/www/lib/plugins/wrap/ && \
    rm -rf stable.zip
    
RUN echo "cgi.fix_pathinfo = 0;" >> /etc/php/7.0/fpm/php.ini
RUN sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php/7.0/fpm/php-fpm.conf
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN rm /etc/nginx/sites-enabled/*
ADD dokuwiki.conf /etc/nginx/sites-enabled/    
    
ADD supervisord.conf /etc/supervisord.conf
ADD start.sh /start.sh
RUN chmod +x /start.sh

EXPOSE 80
VOLUME ["/var/dokuwiki-storage"]

CMD /start.sh
