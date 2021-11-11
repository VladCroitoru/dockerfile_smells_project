FROM ubuntu:14.04
MAINTAINER Shisei Hanai<ruimo.uno@gmail.com>

RUN apt-get update
RUN apt-get install -y wget

# Set nginx mainline repository
RUN cd /tmp && \
  wget http://nginx.org/keys/nginx_signing.key && \
  sudo apt-key add nginx_signing.key

RUN echo "deb http://nginx.org/packages/mainline/ubuntu/ trusty nginx" >> /etc/apt/sources.list
RUN echo "deb-src http://nginx.org/packages/mainline/ubuntu/ trusty nginx" >> /etc/apt/sources.list

RUN apt-get update
RUN apt-get install -y nginx w3m

ADD default.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
EXPOSE 443

CMD ["/usr/sbin/nginx", "-g", "daemon off;"]
