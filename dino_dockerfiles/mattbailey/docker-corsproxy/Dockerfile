FROM debian:jessie

MAINTAINER Matt Bailey <m@mdb.io>

RUN apt-get update && \
    apt-get -y install nginx-extras && \
    rm -rf /var/lib/apt/lists/*

# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log
RUN ln -sf /dev/stderr /var/log/nginx/error.log

VOLUME ["/var/cache/nginx"]

COPY nginx.conf /etc/nginx/nginx.conf
COPY start.sh /start.sh
RUN chmod 744 /start.sh

EXPOSE 80 443

CMD ["/start.sh"]
