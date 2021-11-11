# Version: 0.0.1
FROM ubuntu:14.04
MAINTAINER Olaf Brandt "olaf.brandt@gmail.com"
RUN apt-get update
RUN apt-get install -y nginx
RUN echo 'Olaf Says: Hi, I am in your container. Hello cruel world!' \
    >/usr/share/nginx/html/index.html
COPY fib.linux /usr/local/bin/
