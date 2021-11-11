FROM nginx:latest
MAINTAINER brian.kirkland@live.com

COPY nginx/nginx.conf /etc/nginx/nginx.conf
COPY nginx/site.conf /etc/nginx/conf.d/default.conf

ADD . /var/www/html
