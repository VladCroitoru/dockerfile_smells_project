FROM nginx:1.11.10-alpine

MAINTAINER Shaneen31

ADD nginx.conf /etc/nginx/

RUN apk update \
    && apk upgrade \
    && apk add --no-cache bash \
    && adduser -D -H -u 1000 -s /bin/bash www-data

COPY sites/default.conf /etc/nginx/conf.d/default.conf

CMD ["nginx"]

EXPOSE 80 443
