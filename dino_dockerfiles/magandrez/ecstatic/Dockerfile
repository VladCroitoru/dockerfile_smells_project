FROM alpine:latest
LABEL maintainer="Manuel González <magandrez@gmail.com>"

RUN apk update && apk add nginx \
&& rm -f /etc/nginx/conf.d/default.conf

COPY ./nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

VOLUME ["/var/www/html"]

CMD ["nginx","-g","daemon off;"]