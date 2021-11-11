# dekobon/bouncy-nginx:latest
FROM phusion/baseimage:0.9.17
MAINTAINER Elijah Zupancic <elijah@zupancic.name>

# Syslog setup
RUN sed -i '/source s_src {/,/};/d' /etc/syslog-ng/syslog-ng.conf
COPY etc/syslog-ng/conf.d/sources.conf /etc/syslog-ng/conf.d/sources.conf

RUN apt-get update && \
    apt-get upgrade -qy -o Dpkg::Options::="--force-confold" && \
    apt-get -y install nginx curl wget vim && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Setup default Ngnix proxy configuration
COPY etc/nginx/nginx.conf /etc/nginx/nginx.conf
COPY etc/nginx/sites-available-template/default etc/nginx/sites-available/default
COPY etc/nginx/sites-available-template/default etc/nginx/sites-available-template/default

RUN mkdir /etc/service/nginx
COPY etc/service/nginx/run /etc/service/nginx/run
RUN chmod +x /etc/service/nginx/run

RUN mkdir -p /usr/share/nginx/www

COPY usr/local/bin/bounce_nginx /usr/local/bin/bounce_nginx
RUN chmod +x /usr/local/bin/bounce_nginx

# Define mountable directories.
VOLUME ["/etc/nginx/sites-available","/var/log/nginx"]

CMD ["/sbin/my_init"]
