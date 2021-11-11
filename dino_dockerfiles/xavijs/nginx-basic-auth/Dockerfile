FROM nginx:alpine

MAINTAINER Xavier Juan Serrador <xavijs2@gmail.com>

# Custom website files
COPY www /usr/share/nginx/html

# Nginx configuration files
COPY conf/default.conf /etc/nginx/conf.d/default.conf
COPY conf/authnginx/htpasswd /etc/nginx/authnginx/htpasswd
