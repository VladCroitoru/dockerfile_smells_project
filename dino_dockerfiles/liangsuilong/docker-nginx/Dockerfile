FROM ubuntu:16.04

MAINTAINER  Suilong Liang <suilong.liang@worktogether.io>

ENV NGINX_MAJOR 1.12
ENV NGINX_VERSION 1.12.2
ENV NGINX_VERSION_MINOR 0+xenial0
ENV LC_ALL C.UTF-8

# Manually Add Nginx Stable PPA https://launchpad.net/~nginx/+archive/ubuntu/stable
RUN apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 8B3981E7A6852F782CC4951600A6F0A3C300EE8C 

RUN echo "deb http://ppa.launchpad.net/nginx/stable/ubuntu xenial main" > /etc/apt/sources.list.d/nginx.list 
RUN apt-get -y update && \
    apt-get -y install nginx-full=${NGINX_VERSION}-${NGINX_VERSION_MINOR} && \
    rm -f /etc/nginx/sites-enabled/default && \
    rm -rf /var/lib/apt/lists/*

ADD entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh
VOLUME /etc/nginx/sites-enabled/
EXPOSE 80 443
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
CMD ["start"]
