FROM ubuntu
MAINTAINER mikana <fmikana@gmail.com>
RUN apt-get update
RUN apt-get install -y nginx
ADD index.html /usr/share/nginx/html/
ENTRYPOINT /usr/sbin/nginx -g 'daemon off;' -c /etc/nginx/nginx.conf

