from ubuntu:latest

MAINTAINER Filomeno G. Billones Jr <gneiss01@gmail.com>

# Install Ruby
RUN echo "deb http://ftp.us.debian.org/debian wheezy-backports main" >> /etc/apt/sources.list
RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get install -y make g++ ruby-full nodejs ca-certificates libmysqlclient-dev && \
    apt-get -y clean

