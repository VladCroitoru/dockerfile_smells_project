FROM alpine

MAINTAINER RockYuan <RockYuan@gmail.com>

RUN set -x && \
    apk add --no-cache openssl && \
    apk add --no-cache nginx && \
    apk add --no-cache python && \
    ln -sf /dev/stdout /var/log/nginx/access.log && \
    ln -sf /dev/stderr /var/log/nginx/error.log

EXPOSE 80 443

CMD ["nginx", "-g", "daemon off;"]