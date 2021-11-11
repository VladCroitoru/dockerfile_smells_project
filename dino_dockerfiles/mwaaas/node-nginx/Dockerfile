FROM node:5.12

RUN mkdir -p /usr/packages/
RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app

ENV NGINX_VERSION 1.8.1-1~jessie

RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys 573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62 \
	&& echo "deb http://nginx.org/packages/debian/ jessie nginx" >> /etc/apt/sources.list \
	&& apt-get update \
	&& apt-get install --no-install-recommends --no-install-suggests -y \
                       ca-certificates nginx=${NGINX_VERSION} gettext-base \
	&& rm -rf /var/lib/apt/lists/*

# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
	&& ln -sf /dev/stderr /var/log/nginx/error.log

# Copy custom configuration file from the current directory
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80 443 49153

CMD ["nginx", "-g", "daemon off;"]