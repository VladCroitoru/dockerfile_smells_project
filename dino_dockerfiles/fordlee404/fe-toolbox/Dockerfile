FROM node:0.10.40-slim
MAINTAINER Ford Lee <fordlee404@gmail.com>

ENV DEBIAN_FRONTEND noninteractive
ENV USER root

# Setup home environment
RUN mkdir /home/root && chown -R root: /home/root
WORKDIR /home/root
ENV HOME /home/root

RUN apt-get -yqq update
RUN apt-get -yqq install make
RUN apt-get -yqq install python
RUN apt-get -yqq install g++
RUN apt-get -yqq install ruby-full

RUN gem update --system
RUN gem install compass

RUN npm install -g yo
RUN npm install -g grunt-cli
RUN npm install -g bower
RUN npm install -g gulp
RUN npm install -g webpack
RUN npm install -g webpack-dev-server

# Setup dev environment
RUN mkdir /home/root/share
VOLUME /home/root/share
WORKDIR /home/root/share

CMD ["/bin/bash"]
