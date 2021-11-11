FROM scratch
MAINTAINER Munjal Patel <munjal@munpat.com>

ADD ./rootfs.tar /

RUN mkdir -p /var/lib/nginx
RUN rm /etc/nginx/nginx.conf /etc/nginx/mime.types
RUN mkdir /etc/nginx/ssl

ADD ./config/nginx.conf /etc/nginx/nginx.conf
ADD ./config/mime.types /etc/nginx/mime.types
ADD ./config/default /etc/nginx/sites-enabled/default
ADD ./config/default-ssl /etc/nginx/sites-available/default-ssl

RUN mkdir -p /home/app

RUN echo 'nginx:' `nginx -v`
EXPOSE 80 443
WORKDIR /home/app
CMD ["nginx"]
