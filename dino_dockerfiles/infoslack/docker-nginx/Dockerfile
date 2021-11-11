FROM infoslack/buildpack-deps

MAINTAINER Daniel Romero <infoslack@gmail.com>

RUN wget -q -O - http://nginx.org/keys/nginx_signing.key | sudo apt-key add -

RUN echo "deb http://nginx.org/packages/ubuntu/ trusty nginx" >> /etc/apt/sources.list.d/nginx.list

RUN apt-get update && apt-get install -y nginx && rm -rf /var/lib/apt/lists/*

# forward logs access and errors to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log
RUN ln -sf /dev/stderr /var/log/nginx/error.log

VOLUME ["/var/cache/nginx"]

EXPOSE 80 443

CMD ["nginx", "-g", "daemon off;"]
