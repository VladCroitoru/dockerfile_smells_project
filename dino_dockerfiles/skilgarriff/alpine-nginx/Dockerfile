FROM alpine:latest

MAINTAINER Sean Kilgarriff <seanpkilgarriff@gmail.com>

#Install Nginx and remove the cache because we won't be installing it twice.
RUN apk --no-cache add nginx

#Add custom nginx config file.
COPY ./nginx.conf /etc/nginx/nginx.conf

#Add default config for 1 server.
COPY ./default.conf /etc/nginx/conf.d/default.conf

USER nobody

CMD ["nginx", "-g", "daemon off;"]
