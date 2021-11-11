FROM ubuntu

MAINTAINER Milan Aleksic 

RUN apt-get -y update && apt-get -y install curl vim

RUN curl -L https://www.opscode.com/chef/install.sh | bash

ENV EDITOR=vim

WORKDIR /

RUN mkdir .chef
RUN echo "log_level   dd  :info"  >> .chef/knife.rb
RUN echo "log_location  STDOUT" >> .chef/knife.rb
