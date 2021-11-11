FROM ubuntu
MAINTAINER masanara <masanara@gmail.com>
RUN apt-get install -y nginx
ADD index.html /usr/share/nginx/html/
ADD index2.html /usr/share/nginx/html/
ADD secret /usr/share/nginx/html/
ENTRYPOINT /usr/sbin/nginx -g 'daemon off;' -c /etc/nginx/nginx.conf
