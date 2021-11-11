FROM ubuntu
MAINTAINER LZ
RUN apt-get update
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get install -y nginx git
RUN rm -rf /var/www/html/*
RUN git clone https://github.com/diranetafen/static-website-example.git /var/www/html/
ENTRYPOINT ["/usr/sbin.nginx", "-g" , "daemon off"]
