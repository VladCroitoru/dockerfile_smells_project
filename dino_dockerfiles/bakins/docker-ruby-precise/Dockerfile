FROM ubuntu:12.04
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list
RUN apt-get update
ENV DEBIAN_FRONTEND noninteractive
RUN ( apt-get install -y ruby1.9.1-full make && apt-get install -y ruby1.9.1-full make )
RUN gem install bundler
