FROM nginx:1.9

MAINTAINER Antonio Esposito "kobe@member.fsf.org"

RUN rm -rf /etc/nginx/conf.d/*

RUN chmod 777 /var/cache/nginx

USER nginx
COPY proxy_params nginx.conf /etc/nginx/
