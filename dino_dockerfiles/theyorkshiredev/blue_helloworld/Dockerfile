#
# Docker Hello World image on a BLUE background
# Adapted from https://github.com/docker/dockercloud-hello-world
#
# (c) 2018 - Steven Cooney
###################################################################

FROM alpine:3.7

RUN apk --update --no-cache add nginx php5-fpm && \
    mkdir -p /run/nginx

ADD www /www
ADD nginx.conf /etc/nginx/
ADD php-fpm.conf /etc/php5/php-fpm.conf
ADD run.sh /run.sh

ENV LISTEN_PORT=80

EXPOSE 80
CMD /run.sh
