FROM logicify/centos7:latest
MAINTAINER Dmitry Berezovsky "corvis.mail@gmail.com"

RUN yum -y update \
    && yum -y install nginx

# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log
RUN ln -sf /dev/stderr /var/log/nginx/error.log

COPY ./nginx.conf /etc/nginx/nginx.conf
COPY ./mime.types /etc/nginx/mime.types

ADD sites-enabled/ /etc/nginx/sites-enabled
ADD static/ /var/www

RUN rm -f /var/www/.gitpreserve

EXPOSE 80 443

CMD ["nginx", "-g", "daemon off;"]
