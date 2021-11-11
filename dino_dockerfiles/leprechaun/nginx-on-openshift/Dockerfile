FROM nginx:alpine

ADD make-writable /usr/local/bin/
RUN chmod 755 /usr/local/bin/make-writable

RUN mkdir -p /var/cache/nginx/client_temp && chgrp 0 /var/cache/nginx/client_temp
RUN mkdir -p /var/cache/nginx/proxy_temp && chgrp 0 /var/cache/nginx/proxy_temp
RUN mkdir -p /var/cache/nginx/fastcgi_temp && chgrp 0 /var/cache/nginx/fastcgi_temp
RUN mkdir -p /var/cache/nginx/uwsgi_temp && chgrp 0 /var/cache/nginx/uwsgi_temp
RUN mkdir -p /var/cache/nginx/scgi_temp && chgrp 0 /var/cache/nginx/scgi_temp

# More openshift stuff
RUN sed -i -e 's/user  nginx;/#user nginx;/g' /etc/nginx/nginx.conf
RUN sed -i -e 's/80;/8080;/g' /etc/nginx/conf.d/default.conf
RUN sed -i -e 's:/var/run/nginx.pid:/tmp/nginx.pid:g' /etc/nginx/nginx.conf
RUN chgrp -R 0 /var/run/
RUN chmod -R 777 /var/run

EXPOSE 8080
