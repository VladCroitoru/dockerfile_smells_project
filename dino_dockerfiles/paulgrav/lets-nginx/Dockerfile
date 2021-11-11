FROM debian:jessie
MAINTAINER Paul Grave <paul@stomer.net>

RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys 573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62
RUN echo "deb http://nginx.org/packages/mainline/debian/ jessie nginx" >> /etc/apt/sources.list

ENV NGINX_VERSION 1.9.9-1~jessie

RUN apt-get update && \
apt-get install -y ca-certificates nginx=${NGINX_VERSION} && \
apt-get install -y libffi-dev && \
apt-get install -y python-dev && \
apt-get install -y python-pip && \
apt-get install -y libssl-dev && \
apt-get install -y curl && \
apt-get install -y python-virtualenv && \
apt-get install -y dialog && \
rm -rf /var/lib/apt/lists/* 

RUN virtualenv venv
RUN . venv/bin/activate && pip install -U letsencrypt


# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log
RUN ln -sf /dev/stderr /var/log/nginx/error.log

VOLUME ["/var/cache/nginx"]

# used for webroot reauth
RUN mkdir -p /etc/letsencrypt/webrootauth

ADD entrypoint.sh /entrypoint.sh

EXPOSE 80 443

ENTRYPOINT ["/entrypoint.sh"]
