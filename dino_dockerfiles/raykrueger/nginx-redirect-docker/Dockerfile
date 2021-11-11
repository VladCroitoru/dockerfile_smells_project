FROM nginx:1.13.10-alpine

RUN rm -f /etc/nginx/conf.d/*.conf
ADD ./redirect.conf /etc/nginx/conf.d/

EXPOSE 80
