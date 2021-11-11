# Nginx Lua module to send access logs into elasticsearch
#
VERSION 1.0

FROM yandex/ubuntu:14.04
MAINTAINER Alexander Kushnarev <avkushnarev@gmail.com>

# Nginx
RUN add-apt-repository ppa:nginx/stable
RUN apt-get update
RUN apt-get install -y lua-cjson lua-socket nginx-extras python-mako

# Elastic module
ADD nginx.conf.mako /tmp/
ADD stat_sender.lua /usr/share/nginx/

EXPOSE 80

CMD mako-render /tmp/nginx.conf.mako > /etc/nginx/nginx.conf && nginx
