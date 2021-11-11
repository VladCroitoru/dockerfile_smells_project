FROM node:8.2-slim

MAINTAINER Konstantin Alexandroff <k.alexandroff@gmail.com>

ENV NPM_CONFIG_LOGLEVEL warn

RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys E1DD270288B4E6030699E45FA1715D88E1DF1F24
RUN /bin/bash -c "echo 'deb http://ppa.launchpad.net/git-core/ppa/ubuntu trusty main' > /etc/apt/sources.list.d/git.list"
RUN apt-get update 

RUN apt-get -y install git \
	&& npm install -g --unsafe-perm webpack file-loader \
	&& npm install -g --unsafe-perm elm@0.18 \
	&& npm install -g --unsafe-perm elm-test@0.18 \
	&& npm install -g --unsafe-perm bower \
	&& npm install -g --unsafe-perm elm-github-install \
	&& npm install --save elm-webpack-loader
