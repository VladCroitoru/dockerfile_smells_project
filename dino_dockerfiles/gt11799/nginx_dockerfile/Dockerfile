# Version: 0.0.1
FROM ubuntu:14.04
MAINTAINER Bruce "gting405@163.com"
RUN apt-get update
RUN apt-get install -y nginx
RUN echo 'Hi, I am in your container' >/usr/share/nginx/html/index.html
EXPOSE 80
ENV GO_PATH /home/go-work
ADD ./ /opt/webapp/dockers/
WORKDIR /opt/webapp/dockers
CMD ["nginx", "-g", "daemon off;"]
