FROM node:6.2.2

MAINTAINER Emiliano Jankowski

RUN apt-get update && \
    apt-get install -y vim curl git 

# Install Ruby
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3 && \
    \curl -sSL https://get.rvm.io | bash -s stable --ruby --with-default-gems="sass compass"

RUN npm install -g bower gulp
