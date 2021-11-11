FROM ubuntu:14.04
MAINTAINER Foo Bar <tarryjenny@gmail.com>
 
RUN apt-get update
RUN apt-get install -y nginx
RUN echo "\ndaemon on;" >> /etc/nginx/nginx.conf
RUN chown -R www-data:www-data /var/lib/nginx
 
VOLUME ["/data", "/etc/nginx/site-enabled", "/var/log/nginx"]
 
WORKDIR /etc/nginx
 
CMD ["nginx"]
 
EXPOSE 80
EXPOSE 443
EXPOSE 8080
