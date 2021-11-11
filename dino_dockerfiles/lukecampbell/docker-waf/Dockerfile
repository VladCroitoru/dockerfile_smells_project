FROM nginx

MAINTAINER Luke Campbell <luke.campbell@rpsgroup.com>

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx /etc/nginx
VOLUME ["/usr/share/nginx/html/waf"]
