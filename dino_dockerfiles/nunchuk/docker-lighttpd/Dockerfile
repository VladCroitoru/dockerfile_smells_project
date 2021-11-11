############################################################ 
# Dockerfile to build lighttpd image
# Based on alpine
############################################################

FROM nunchuk/aliyun-alpine:3.4
MAINTAINER XinYe <nunchuk@live.com>

RUN apk add -U lighttpd \
    && rm -rf /var/cache/apk/*

RUN echo server.network-backend = \"writev\" >> /etc/lighttpd/lighttpd.conf

EXPOSE 80
VOLUME /var/www/localhost

CMD ["lighttpd", "-D", "-f", "/etc/lighttpd/lighttpd.conf"]