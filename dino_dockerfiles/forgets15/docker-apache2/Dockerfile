FROM gliderlabs/alpine:3.1
MAINTAINER I-Ching Wang <forgets15@gmail.com>
RUN apk --update add apache2
ENTRYPOINT ["/usr/sbin/apachectl", "-f", "/etc/apache2/httpd.conf", "-e", "info", "-DFOREGROUND"]
