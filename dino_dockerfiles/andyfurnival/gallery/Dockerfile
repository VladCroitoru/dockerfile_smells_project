FROM andyfurnival/nginx:master

MAINTAINER Andy Furnival


COPY Gallery /var/www/gallery
RUN chmod 755 /var/www/gallery
RUN chmod 755 /var/www/gallery/*

RUN chown nginx:nginx /var/www/gallery
RUN chown nginx:nginx /var/www/gallery/*

ADD ./sites-enabled/nginx.static.conf /etc/nginx/sites-enabled/nginx.static.conf

CMD /usr/local/sbin/nginx