FROM        nginx:latest

MAINTAINER  tdeheurles@gmail.com

RUN         rm /etc/nginx/conf.d/*.conf

COPY        nginx.conf        /etc/nginx/

COPY        src/www/          /www/
COPY        out/bundle.js     /www/javascripts/
