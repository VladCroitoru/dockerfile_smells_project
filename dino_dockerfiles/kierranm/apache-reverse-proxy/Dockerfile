FROM phusion/baseimage:0.9.16
MAINTAINER Kierran McPherson <kierranm@gmail.com>
ENV DEBIAN_FRONTEND noninteractive

EXPOSE 80

# install the required packages
RUN apt-get update && sudo apt-get install -y \
      build-essential \
      apache2 \
      libapache2-mod-proxy-html \
      libxml2-dev

VOLUME /sites-enabled

# enable the proxy modules
RUN a2enmod proxy \
			proxy_http \
			proxy_ajp \
			rewrite \
			deflate \
			headers \
			proxy_balancer \
			proxy_connect \
			proxy_html \
      ssl

# add the startup config file
RUN mkdir -p /etc/my_init.d
ADD Assets/config.sh /etc/my_init.d/config.sh
RUN chmod +x /etc/my_init.d/config.sh

# add apache to runit
RUN mkdir /etc/service/apache
ADD Assets/apache.sh /etc/service/apache/run
RUN chmod +x /etc/service/apache/run

# use phusion/baseimage init system
CMD ["/sbin/my_init"]
