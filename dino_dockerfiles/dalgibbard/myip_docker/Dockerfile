FROM alpine
MAINTAINER Darren Gibbard <dalgibbard@gmail.com>
RUN apk --update --no-cache add --repository http://dl-cdn.alpinelinux.org/alpine/edge/main --repository http://dl-cdn.alpinelinux.org/alpine/edge/community \
  lighttpd \
  php7-common \
  php7-cgi \
  fcgi \
  php7-posix \
  php7-gettext && \
  rm -rf /var/cache/apk/*
RUN adduser www-data -G www-data -H -s /bin/false -D
RUN mkdir /run/lighttpd && chown www-data /run/lighttpd
COPY lighttpd.conf /etc/lighttpd/lighttpd.conf
COPY docker-entrypoint.sh /
COPY index.php /var/www/
EXPOSE 80
ENTRYPOINT ["/docker-entrypoint.sh"]
