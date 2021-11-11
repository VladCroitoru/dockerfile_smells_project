FROM alpine:3.4

# install
RUN apk --update add apache2 \
 && rm -f /var/cache/apk/* 

# configure
RUN mkdir -p /run/apache2 \
 && ln -s /dev/stderr /var/log/apache2/error.log \
 && ln -s /dev/stdout /var/log/apache2/access.log

COPY httpd.conf /etc/apache2/httpd.conf
COPY demo.conf.in /etc/apache2/conf.d/demo.conf.in
COPY src/ /var/www/demo/
COPY entrypoint.sh /usr/local/bin/entrypoint.sh

RUN chmod +x /usr/local/bin/entrypoint.sh

EXPOSE 80

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

CMD ["httpd", "-DFOREGROUND"]