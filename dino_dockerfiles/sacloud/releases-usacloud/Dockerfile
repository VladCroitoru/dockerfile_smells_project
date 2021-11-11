FROM nginx:1.13
MAINTAINER Kazumichi Yamamoto <yamamoto.febc@gmail.com>
LABEL MAINTAINER 'Kazumichi Yamamoto <yamamoto.febc@gmail.com>'

ENV NGINX_ROOT_DIR=/usr/share/nginx/html

COPY default.conf /etc/nginx/conf.d/default.conf
COPY status.html ${NGINX_ROOT_DIR}/
COPY bin ${NGINX_ROOT_DIR}/bin
COPY repos ${NGINX_ROOT_DIR}/repos
COPY bin/usacloud_windows-386.zip bin/usacloud_windows-amd64.zip ${NGINX_ROOT_DIR}/repos/windows/
COPY contrib/completion/bash/usacloud ${NGINX_ROOT_DIR}/contrib/completion/bash/usacloud
