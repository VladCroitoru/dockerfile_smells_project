FROM nginx:1.13
MAINTAINER Kazumichi Yamamoto <yamamoto.febc@gmail.com>
LABEL MAINTAINER 'Kazumichi Yamamoto <yamamoto.febc@gmail.com>'

ENV NGINX_ROOT_DIR=/usr/share/nginx/html

COPY default.conf /etc/nginx/conf.d/default.conf
COPY status.html ${NGINX_ROOT_DIR}/
COPY bin/* ${NGINX_ROOT_DIR}/
