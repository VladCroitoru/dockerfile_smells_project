FROM alpine

MAINTAINER NGINX Docker Maintainers "docker-maint@nginx.com"

RUN apk add --update nginx && rm -rf /var/cache/apk/*

# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log
RUN ln -sf /dev/stderr /var/log/nginx/error.log

VOLUME ["/var/cache/nginx"]

# add my configuration files
ADD nginx.conf /etc/nginx/nginx.conf
ADD domain.conf /etc/nginx/conf.d/domain.conf

EXPOSE 80 443

CMD ["nginx", "-g", "daemon off;"]
