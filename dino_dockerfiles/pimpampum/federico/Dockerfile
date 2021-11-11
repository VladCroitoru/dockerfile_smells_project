FROM ubuntu
MAINTAINER davidsis205

RUN echo "deb http://nginx.org/packages/ubuntu/ trusty nginx" >> /etc/apt/sources.list \
  && apt-get update \
  && apt-get install -y --allow-unauthenticated ca-certificates nginx gettext-base \
  && rm -rf /var/lib/apt/lists/*

VOLUME ["/etc/nginx/sites-enabled", "/etc/nginx/certs", "/etc/nginx/conf.d", "/var/log/nginx", "/var/www/html"]

WORKDIR /etc/nginx

EXPOSE 80 443

CMD ["nginx", "-g"]
