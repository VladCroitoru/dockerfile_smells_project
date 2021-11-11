FROM alpine:latest

RUN apk add --no-cache lighttpd
EXPOSE 80

WORKDIR /var/www
ENTRYPOINT ["lighttpd-angel", "-D", "-f", "lighttpd.conf"]

ADD lighttpd.conf lighttpd.conf
RUN lighttpd -t -f lighttpd.conf

VOLUME /var/www/default
