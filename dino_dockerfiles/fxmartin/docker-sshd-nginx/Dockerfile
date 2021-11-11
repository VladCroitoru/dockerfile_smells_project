##############################################################################
# Dockerfile for building docker container with passwordless sshd server and
# nginx serving static page. This is mostly a template for creating more
# useful docker images.
#
# Build with docker build -t fxmartin/docker-sshd-nginx .
#
# Syncordis Copyright 2016
# Author: FX
# Date: 10-mar-2016
# Version: 1.11
##############################################################################

FROM ubuntu:trusty

# Maintainer details
MAINTAINER fxmartin <fxmartin@syncordisconsulting.com>

# Avoid ERROR: invoke-rc.d: policy-rc.d denied execution of start.
RUN echo "#!/bin/sh\nexit 0" > /usr/sbin/policy-rc.d

# Set-up environment variables to fix encoding

# Default to UTF-8 file.encoding
# Set the locale - from http://jaredmarkell.com/docker-and-locales/
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8 

# Workaround for https://github.com/docker/docker/issues/9299
ENV TERM xterm

# install sshd, nginx and supervisor
RUN apt-get update && apt-get install -y \
	openssh-server \
	supervisor nginx && \
	apt-get autoremove && apt-get autoclean && apt-get clean -y

# configure sshd with passwordless auth
ADD ssh_keys/id_rsa_docker.pub /tmp/id_rsa_docker.pub
RUN mkdir -p /var/run/sshd && \
	mkdir -p /root/.ssh && \
	cat /tmp/id_rsa_docker.pub >> /root/.ssh/authorized_keys && \
	rm /tmp/id_rsa_docker.pub

# configure nginx to serve static page
RUN echo "daemon off;" >> /etc/nginx/nginx.conf && \
	mkdir -p /var/www
ADD nginx/default           /etc/nginx/sites-available/default
ADD nginx/index.html        /var/www/index.html

# configure nginx to serve supervisord
RUN echo "[inet_http_server]" >> /etc/supervisor/supervisord.conf && \
	echo "port=127.0.0.1:9001" >> /etc/supervisor/supervisord.conf && \
	echo "username=admin" >> /etc/supervisor/supervisord.conf && \
	echo "password=admin" >> /etc/supervisor/supervisord.conf

ADD nginx/supervisord /etc/nginx/sites-available/supervisord
RUN ln -s /etc/nginx/sites-available/supervisord /etc/nginx/sites-enabled/supervisord

# configure supervisor
RUN mkdir -p /var/log/supervisor
ADD supervisor/sshd.conf   /etc/supervisor/conf.d/sshd.conf
ADD supervisor/nginx.conf   /etc/supervisor/conf.d/nginx.conf

#clean-up
RUN apt-get clean

EXPOSE 22
EXPOSE 80
EXPOSE 91

CMD ["/usr/bin/supervisord", "-n"]