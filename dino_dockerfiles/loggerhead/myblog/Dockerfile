FROM quay.io/wunder/fuzzy-alpine-nginx-pagespeed
MAINTAINER loggerhead "lloggerhead@gmail.com"

ENV HOME /home/root
WORKDIR /home/root

RUN apk add --no-cache bash git python py-pip ;\
    pip install flask supervisor

ADD nginx-config /etc/nginx
ADD update-site /var/www/blog/myblog-update
ADD supervisord.conf /etc/supervisor/supervisord.conf
RUN git clone https://github.com/loggerhead/blog.loggerhead.me.git /var/www/blog/output

VOLUME ["/etc/nginx", "/var/www/blog/cert", "/var/log/nginx", "/var/run/nginx", "/var/cache/nginx"]

ENTRYPOINT ["supervisord"]
