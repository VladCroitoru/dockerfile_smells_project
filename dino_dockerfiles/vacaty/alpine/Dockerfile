FROM alpine:3.6

RUN set -ex \
    && addgroup -g 82 -S www-data && adduser -u 82 -S -D -G www-data www-data \
    && sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories \
    \
    && echo "export PS1='\033]0;\w\a\n\033[33m\t \033[32m\u@\h \033[33m\w\033[0m\n\$ '" >> /etc/profile \
    && echo "alias ll='ls -l'" >> /etc/profile \
    \
    && apk add --no-cache su-exec bash curl zip xz wget tzdata \
    && cp -f /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && apk del tzdata \
    \
    && mkdir -p /conf /data /log

COPY docker-* /usr/local/bin/
ENTRYPOINT ["docker-entrypoint"]

