FROM debian:jessie

MAINTAINER Aria2 Docker Maintainers "charlie@cokapp.com"

ENV NGINX_VERSION 1.11.1-1~jessie

RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys 573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62 \
	&& echo "deb http://nginx.org/packages/mainline/debian/ jessie nginx" >> /etc/apt/sources.list \
	&& apt-get update \
	&& apt-get install --no-install-recommends --no-install-suggests -y \
						nginx=${NGINX_VERSION} \
						wget \
						ca-certificates \
						aria2 \
	&& rm -rf /var/lib/apt/lists/*

# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
	&& ln -sf /dev/stderr /var/log/nginx/error.log

#webui
COPY yaaw-zh-hans/public_html /usr/share/nginx/html

#aria2.conf
ADD aria2.conf /etc/aria2/
#start.sh
ADD start.sh /etc/aria2/

#data
VOLUME ["/etc/aria2/data"]

EXPOSE 80
EXPOSE 6800

WORKDIR /etc/aria2

CMD ["/bin/bash", "/etc/aria2/start.sh"]