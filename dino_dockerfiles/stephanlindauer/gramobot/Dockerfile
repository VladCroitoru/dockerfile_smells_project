FROM ubuntu:trusty

MAINTAINER stephan lindauer <stephanlindauer@posteo.de>

RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get -y install nodejs nodejs-legacy npm
RUN apt-get clean

RUN npm install -g brunch
RUN npm install -g bower

ADD . /gramobot/

RUN chmod +x ./gramobot/install.sh
#
# CMD ./gramobot/install.sh
