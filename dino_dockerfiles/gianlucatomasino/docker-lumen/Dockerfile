FROM alpine:3.3
RUN apk --update add php-apache2 php-pdo php-json && mkdir /run/apache2
COPY conf/httpd.conf /etc/apache2/httpd.conf

WORKDIR /app

EXPOSE 80

CMD httpd -D FOREGROUND
