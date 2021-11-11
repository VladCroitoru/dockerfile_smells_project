FROM ubuntu:15.10
MAINTAINER  Sylvain Lasnier <sylvain.lasnier@gmail.com>

# Add useful packages
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get -y upgrade && apt-get -y install curl bash-completion vim-tiny supervisor wget aptitude && apt-get clean

# Setup root password for login process
RUN echo root:root | chpasswd

# Language setup
RUN locale-gen  fr_FR.UTF-8 en_US.UTF-8
RUN update-locale LANG=en_US.UTF-8

# Common alias
RUN alias ls='ls --color=auto'
RUN alias ll='ls -halF'

# Volume
VOLUME /data
