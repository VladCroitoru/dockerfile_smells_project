FROM nginx:1.10-alpine
MAINTAINER koudaiii "cs006061@gmail.com"

RUN mkdir -p /var/www/nginx-default

COPY files/nginx-docker.conf /etc/nginx/conf.d/
COPY files/http_gzip_static.conf /etc/nginx/conf.d/
COPY files/nginx.conf /etc/nginx/
COPY files/domain.crt /etc/nginx/conf.d/
COPY files/domain.key /etc/nginx/conf.d/
COPY files/nginx.htpasswd /etc/nginx/conf.d/nginx.htpasswd
COPY files/status.html /var/www/nginx-default/
COPY files/run.sh /run.sh

RUN rm -f /etc/nginx/conf.d/default.conf
RUN apk --update add curl tzdata && \
    cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime && \
    apk del tzdata && \
    rm -rf /var/cache/apk/*

CMD ["./run.sh"]
