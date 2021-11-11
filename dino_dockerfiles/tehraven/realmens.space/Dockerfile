FROM tehraven/alpinewebos
MAINTAINER "https://github.com/tehraven"

#Server Hacks

ADD servers/web-root /

RUN chown www-data:www-data /etc/nginx/*.pem \
    && chown www-data:www-data /etc/nginx/*.key \
    && rm -rf /etc/php7/conf.d/opcache.ini \
    && touch /var/log/nginx/access.log \
    && touch /var/log/nginx/error.log \
    && chown www-data:www-data /var/log/nginx/*.log \
    && chmod -R 0777 /var/log/nginx \
    && composer global require "hirak/prestissimo:^0.3"

ADD servers/web /var/www
WORKDIR /var/www
RUN rm -rf eve-esi-master/docs \
    && rm -rf eve-esi-master/test \
    && chown -R www-data:www-data /var/www
    
ENV DNSMASQ_DEFAULT 0
ENV DNSMASQ_SERVERS 8.8.8.8,8.8.4.4
EXPOSE 80

ENTRYPOINT ["/init"]
CMD []