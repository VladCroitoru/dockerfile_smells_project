FROM phusion/baseimage
MAINTAINER johnodon <johnodon68@gmail.com>
ENV DEBIAN_FRONTEND noninteractive

# Set correct environment variables
ENV HOME /root

# Use baseimage-docker's init system
CMD ["/sbin/my_init"]

# Change uid & gid to match Unraid
RUN usermod -u 99 nobody && \
    usermod -g 100 nobody

RUN apt-get update -qq
RUN apt-get install wget -qy
ADD /init /etc/my_init.d/
RUN chmod +x /etc/my_init.d/install.sh

# Port and Volume mappings
VOLUME /home/nobody
EXPOSE 80
