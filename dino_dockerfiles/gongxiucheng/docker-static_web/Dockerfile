# Version:0.0.1
FROM ubuntu:14.04
MAINTAINER gongxiucheng "gongxiucheg@vargo.com.cn"
RUN apt-get update && apt-get install -y nginx
RUN echo 'hi,i am in your container' > /usr/share/nginx/html/index.html
EXPOSE 80
