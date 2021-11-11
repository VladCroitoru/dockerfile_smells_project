FROM ubuntu
MAINTAINER yusuke <you_oki1@yahoo.co.jp>
RUN apt-get update
RUN apt-get install -y nginx
ADD index.html /usr/share/nginx/html/
ENTRYPOINT /usr/sbin/nginx -g 'daemon off;' -c /etc/nginx/nginx.conf
