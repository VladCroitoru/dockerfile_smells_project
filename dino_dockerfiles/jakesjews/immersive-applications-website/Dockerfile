FROM ubuntu:latest

MAINTAINER Immersive Applications

RUN apt-get update
RUN apt-get install nginx -y
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

ADD . /var/www/html

EXPOSE 80
CMD /usr/sbin/nginx
