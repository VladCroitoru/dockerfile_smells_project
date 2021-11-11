FROM liverbool/docker-base

MAINTAINER  Liverbool "nukboon@gmail.com"

RUN apt-get install -y nginx
RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf

# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log
RUN ln -sf /dev/stderr /var/log/nginx/error.log

ADD vhost.conf /etc/nginx/sites-enabled/default

WORKDIR /etc/nginx

 EXPOSE 80 443

ADD init.sh /
RUN chmod 755 /init.sh

CMD ["/init.sh"]
