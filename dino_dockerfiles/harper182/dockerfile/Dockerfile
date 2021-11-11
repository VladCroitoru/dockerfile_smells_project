#version:0.0.1
FROM ubuntu:latest
MAINTAINER harper "harper@gmail.com"
RUN apt-get update
RUN apt-get install -y nginx

RUN mkdir -p /usr/share/nignx/html/
RUN echo 'Hi,i am in your container'\
	> /usr/share/nignx/html/index.html
EXPOSE 80
