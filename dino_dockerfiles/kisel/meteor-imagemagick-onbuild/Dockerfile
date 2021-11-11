FROM debian:wheezy
MAINTAINER kisel
RUN apt-get update && apt-get install -y imagemagick curl bzip2 build-essential python git vim-tiny && apt-get clean
RUN curl -sL https://install.meteor.com | sed s/--progress-bar/-sL/g | /bin/sh
