FROM alpine:3.4

# install
RUN apk --update add apache2 \
                     apache2-proxy \
 && rm -f /var/cache/apk/* 

# configure
RUN mkdir -p /run/apache2 \
 && mkdir -p /var/cache/apache2/mod_cache_disk \
 && chown apache:apache /var/cache/apache2/mod_cache_disk \
 && ln -s /dev/stderr /var/log/apache2/error.log \
 && ln -s /dev/stdout /var/log/apache2/access.log

COPY proxy.conf.in /etc/apache2/conf.d/proxy.conf.in
COPY entrypoint.sh /usr/local/bin/entrypoint.sh

RUN chmod +x /usr/local/bin/entrypoint.sh

EXPOSE 80

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

CMD ["-D", "FOREGROUND"]