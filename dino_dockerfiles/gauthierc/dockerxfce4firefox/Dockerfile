# This file describes how to build Plone into a runnable linux container with all dependencies installed
# To build:
# 1) Install docker (http://docker.io)
# 2) Run:
# docker run -d <imageid>
#
# VERSION                0.3
# DOCKER-VERSION        1.3.2

from       gauthierc/dockerspicexfce4 
MAINTAINER Gauthier C.
run        DEBIAN_FRONTEND=noninteractive apt-get update && apt-get -y install firefox firefox-locale-fr
VOLUME	   ["/home"]
expose     5900
cmd        /root/run.sh
