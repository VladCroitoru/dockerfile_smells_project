FROM alpine:3.4

MAINTAINER Rudi Floren <rudi.floren@gmail.com>

RUN apk add --update nginx
RUN apk add --update curl
RUN rm -rf /var/cache/apk/* && rm -rf /tmp/*

ADD nginx.conf /etc/nginx/
ADD app.conf /etc/nginx/conf.d/

RUN echo "upstream php-upstream { server php:9001; }" > /etc/nginx/conf.d/upstream.conf
RUN curl -sLo /usr/local/bin/ep https://github.com/kreuzwerker/envplate/releases/download/v0.0.8/ep-linux && chmod +x /usr/local/bin/ep

RUN adduser -D -g '' -G www-data www-data

CMD [ "/usr/local/bin/ep", "-v", "/etc/nginx/nginx.conf", "/etc/nginx/conf.d/*.conf", "--", "/usr/sbin/nginx" ]

EXPOSE 80
EXPOSE 443
