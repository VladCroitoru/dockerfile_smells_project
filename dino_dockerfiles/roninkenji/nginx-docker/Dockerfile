FROM alpine:latest
MAINTAINER roninkenji

EXPOSE 80
EXPOSE 443

# Expected Host mounts "/config", "/var/log/nginx", "/var/www"

RUN apk update && apk upgrade && apk add nginx && rm -rf /var/cach/apk/*

COPY docker_init.sh /usr/local/bin/docker_init.sh
RUN chmod +x /usr/local/bin/docker_init.sh
# ADD https://github.com/Neilpang/acme.sh/archive/2.7.2.zip /tmp

ENTRYPOINT /usr/local/bin/docker_init.sh
