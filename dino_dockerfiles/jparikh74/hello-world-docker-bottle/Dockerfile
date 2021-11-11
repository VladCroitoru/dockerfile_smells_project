# A super-simple "hello world" server that exposes port 8080
#
# VERSION               0.1.0
FROM ubuntu
MAINTAINER Joshua Conner <joshua.conner@gmail.com>

# create user
RUN groupadd web
RUN useradd -d /home/bottle -m bottle

# make sure sources are up to date
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list
RUN apt-get update
RUN apt-get upgrade -y

