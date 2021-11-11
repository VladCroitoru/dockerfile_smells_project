FROM phusion/baseimage:0.9.18

#########################################
##        ENVIRONMENTAL CONFIG         ##
#########################################
# Set correct environment variables
ENV DEBIAN_FRONTEND="noninteractive" HOME="/root" LC_ALL="C.UTF-8" LANG="en_US.UTF-8" LANGUAGE="en_US.UTF-8"

# Use baseimage-docker's init system
CMD ["/sbin/my_init"]

#########################################
##         RUN INSTALL SCRIPT          ##
#########################################
ADD install.sh /tmp/
RUN bash /tmp/install.sh

#########################################
##         EXPORTS AND VOLUMES         ##
#########################################
VOLUME /config
VOLUME /data

EXPOSE 1030/udp 1900/udp 9000/tcp
