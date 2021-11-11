# base image 
# https://github.com/srinigv/docker_base
#
#
# VERSION 1.0

FROM ubuntu:16.04
MAINTAINER srinigv <srinigv@icloud.com>

ENV DEBIAN_FRONTEND noninteractive
ENV LC_ALL C
ENV HOME /root


# enable universe
RUN sed 's/main$/main universe/' -i /etc/apt/sources.list

# copy & install dependencies
ADD install /tmp/install
RUN chmod +x /tmp/install/* && /tmp/install/dependencies.sh && /tmp/install/prepare.sh && rm /tmp/install -rf

# screen
ADD files/screenrc /root/.screenrc

# add next dependencies
ADD files/.vimrc /root/.vimrc
ADD files/.gitconfig /root/.gitconfig

# start & install
ADD files/install.sh /opt/install.sh
RUN mkdir -p /opt/run
RUN chmod +x /opt/install.sh
