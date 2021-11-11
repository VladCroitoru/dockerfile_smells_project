FROM nginx:1.19.3-alpine
ENV TZ=Asia/Shanghai
RUN apk add --no-cache --virtual .build-deps ca-certificates bash curl unzip php7
COPY nginx/default.conf.template /etc/nginx/conf.d/default.conf.template
COPY nginx/nginx.conf /etc/nginx/nginx.conf
COPY nginx/static-html /usr/share/nginx/html/index
COPY nginx/h5-speedtest /usr/share/nginx/html/speedtest
COPY configure.sh /configure.sh
COPY v2ray_config /
RUN chmod +x /configure.sh

ENTRYPOINT ["sh", "/configure.sh"]

