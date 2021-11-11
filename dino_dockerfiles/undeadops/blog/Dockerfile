FROM undeadops/alpine-pyapp

MAINTAINER Mitch Anderson "mitch@metauser.net"

RUN pip install pelican Markdown \
  && adduser -S -s /sbin/nologin -G www-data www-data

ADD . /source

COPY nginx/nginx.conf /etc/nginx/nginx.conf
COPY nginx/default /etc/nginx/sites-enabled/default
COPY nginx/ssl/metauser.net.key /etc/nginx/ssl/
COPY nginx/ssl/metauser.net.pem /etc/nginx/ssl/

WORKDIR /source

RUN pelican ./content/

RUN rm -rf /www/* \
  && cp -R ./output/* /www/

# I don't know if this is needed.. 
CMD ["/usr/sbin/nginx", "-g", "daemon off;"]
