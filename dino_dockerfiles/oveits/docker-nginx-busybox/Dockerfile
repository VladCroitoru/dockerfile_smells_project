FROM progrium/busybox

MAINTAINER Oliver Veits <oliver.veits@web.de>

RUN opkg-install nginx

RUN mkdir /var/lib/nginx
ADD nginx.conf /etc/nginx/nginx.conf
RUN mkdir /usr/html
ADD index.html /usr/html/index.html

EXPOSE 80 443

ENTRYPOINT ["/usr/sbin/nginx"]
