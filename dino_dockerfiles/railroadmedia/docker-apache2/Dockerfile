FROM webdevops/apache:ubuntu-16.04

MAINTAINER Caleb Favor <caleb@drumeo.com>

ARG PHP_SOCKET=127.0.0.1:9000
ENV WEB_PHP_SOCKET=$PHP_SOCKET
ENV WEB_DOCUMENT_ROOT=/var/www

RUN mkdir -p /app

EXPOSE 80 443

WORKDIR /var/www

ENTRYPOINT ["/opt/docker/bin/entrypoint.sh"]

CMD ["supervisord"]