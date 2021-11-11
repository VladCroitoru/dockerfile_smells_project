FROM nginx:latest
MAINTAINER Shan

RUN rm -f /etc/nginx/conf.d/*.conf
ADD ./redirect.conf /etc/nginx/conf.d/
