FROM ubuntu:trusty
MAINTAINER Tatsuro Hisamori <medianetworks@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

# update & base packages
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get -y install build-essential curl git openjdk-7-jdk

# install jruby
RUN curl -L https://s3.amazonaws.com/jruby.org/downloads/1.7.19/jruby-bin-1.7.19.tar.gz | tar zxf -
ENV PATH /jruby-1.7.19/bin:$PATH

# install norikra
RUN gem install norikra --no-ri --no-rdoc

# run norikra
EXPOSE 26571 26578
