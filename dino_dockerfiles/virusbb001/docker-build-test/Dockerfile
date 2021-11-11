FROM ubuntu
MAINTAINER virusbb0001 <virusbb001a@gmail.com>
RUN apt-get install -y nginx
ADD index.html /usr/share/nginx/html/
ENTRYPOINT /usr/sbin/nginx -g 'daemon off;' -c /etc/nginx/nginx.conf
