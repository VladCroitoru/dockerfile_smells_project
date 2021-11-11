# Dockerfile to create a nodejs image with pm2 installed

FROM ubuntu:16.04

RUN apt-get update; apt-get -y upgrade; apt-get install -y apt-utils apt-transport-https
RUN apt-get install -y sudo curl

RUN curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
RUN sudo apt-get update; sudo apt-get install -y nodejs

RUN apt-get install -y build-essential

RUN npm install pm2 -g

RUN sudo env PATH=$PATH:/usr/local/bin pm2 startup upstart

