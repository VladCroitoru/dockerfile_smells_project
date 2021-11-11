FROM debian:latest

MAINTAINER Agnaldo Marinho "agnaldoneto@ufpa.br"

COPY sources.list /etc/apt/sources.list

RUN apt-get update; apt-get -y install gnupg

RUN echo "deb http://nginx.org/packages/debian/ stretch nginx" >> /etc/apt/sources.list.d/nginx.list

RUN apt-key adv --fetch-keys http://nginx.org/keys/nginx_signing.key

RUN apt-get update; apt-get -y install nginx; apt-get clean

RUN ln -sf /dev/stdout  /var/log/nginx/access.log

RUN ln -sf /dev/stderr  /var/log/nginx/error.log

RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf

EXPOSE 8080
EXPOSE 443

STOPSIGNAL SIGTERM


#CMD ["/usr/sbin/nginx"]
CMD ["nginx"]
