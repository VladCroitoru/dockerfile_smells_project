FROM ubuntu:14.04

MAINTAINER Andrew Kimpton "awk@onshape.com"

RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 00A6F0A3C300EE8C
RUN echo "deb [arch=amd64] http://ppa.launchpad.net/nginx/stable/ubuntu/ trusty main" >> /etc/apt/sources.list

RUN apt-get update && \
    apt-get install -y ca-certificates nginx-full && \
    rm -rf /var/lib/apt/lists/*

# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log
RUN ln -sf /dev/stderr /var/log/nginx/error.log

VOLUME ["/var/cache/nginx"]

EXPOSE 80 443

CMD ["nginx", "-g", "daemon off;"]
