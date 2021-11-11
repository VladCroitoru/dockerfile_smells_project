# Version: 0.0.2
FROM ubuntu:14.04
MAINTAINER Gas Creature "angrydog@hotmail.com"
RUN apt-get update
RUN apt-get install -y nginx
RUN echo 'Hi, I am in your container' \
	>/usr/share/nginx/html/index.html
RUN apt-get install -y vim tree
EXPOSE 80
WORKDIR /home/docker
ADD .inputrc /home/docker/.inputrc
ADD .vimrc   /home/docker/.vimrc
ADD .bashrc  /home/docker/.bashrc
COPY bin/    /home/docker/bin/
ENTRYPOINT ["/usr/sbin/nginx"]
CMD ["-g","daemon off;"]
