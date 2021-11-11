FROM alpine:3.4

# install
RUN apk --update add php5-apache2 \
                     php5-cli \
                     php5-json \
 && rm -f /var/cache/apk/* 

# configure
RUN sed -i "s/#LoadModule rewrite_module/LoadModule rewrite_module/" /etc/apache2/httpd.conf \
 && mkdir -p /run/apache2 \
 && ln -s /dev/stderr /var/log/apache2/error.log \
 && ln -s /dev/stdout /var/log/apache2/access.log

COPY smil-origin.conf.in /etc/apache2/conf.d/smil-origin.conf.in
COPY public_src /var/www/smil-origin
COPY entrypoint.sh /usr/local/bin/entrypoint.sh

RUN chmod +x /usr/local/bin/entrypoint.sh

EXPOSE 80

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

CMD ["httpd", "-DFOREGROUND"]
