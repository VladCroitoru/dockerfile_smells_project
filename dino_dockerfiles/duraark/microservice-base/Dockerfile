## FIXXME: check legal implications!
## see http://askubuntu.com/questions/563680/ubuntu-for-docker-containers
FROM dockerimages/ubuntu-core:14.04

MAINTAINER Martin Hecher <martin.hecher@fraunhofer.at>

##
## Base dependencies
##
RUN DEBIAN_FRONTEND=noninteractive
RUN apt-get clean && apt-get update && apt-get install -qqy curl

##
## 'duraark-geometricenrichment' dependencies:
##
RUN apt-get -y install git software-properties-common build-essential cmake vim libboost-program-options1.55-dev libeigen3-dev apt-transport-https ca-certificates curl iptables

##
## 'duraark-digitalpreservation' dependencies:
##
RUN apt-get -y install openjdk-7-jdk

##
## 'duraark-metadata' dependencies:
##
RUN apt-get install python software-properties-common -y && add-apt-repository ppa:fkrull/deadsnakes -y && apt-get update -y && apt-get install python3.3 python3-httplib2 python-httplib2 -y

##
## Docker & docker-compose
##
RUN curl -sSL https://get.docker.com | sh
RUN curl -L https://github.com/docker/compose/releases/download/1.5.1/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose
RUN chmod +x /usr/local/bin/docker-compose

##
## NodeJS 0.12
##
RUN curl -sL https://deb.nodesource.com/setup_0.12 | sudo bash -
RUN apt-get install -y nodejs
RUN npm install -g sails gulp-cli ember-cli nodemon bower grunt-cli

##
## // FIXXME: integrate in block above, this is just added last for a faster rebuild ...
## 'duraark-geometricenrichment' dependencies II:
##
RUN apt-get -y install imagemagick
