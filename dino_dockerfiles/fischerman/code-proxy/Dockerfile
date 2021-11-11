FROM webdevops/apache:ubuntu-16.04

RUN a2enmod proxy proxy_wstunnel proxy_http ssl

RUN mkdir /app

ADD 02-collabora.conf /opt/docker/etc/httpd/vhost.common.d/

ENV WEB_ALIAS_DOMAIN=office.local
ENV WEB_DOCUMENT_ROOT=/app