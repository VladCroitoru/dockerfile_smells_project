FROM ubuntu:14.04

MAINTAINER Jeroen Van den Berghe <vandenberghe.jeroen@gmail.com>

RUN apt-get update && apt-get install -y \
	git-core \
	curl \
	wget \
	default-jre

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
RUN sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'

RUN apt-get update && apt-get install -y \
	firefox \
	google-chrome-stable \
	xvfb \
	libgl1-mesa-dri \
	xfonts-100dpi xfonts-75dpi xfonts-scalable xfonts-cyrillic

RUN git clone https://github.com/creationix/nvm.git /.nvm
RUN echo ". /.nvm/nvm.sh" >> /etc/bash.bashrc
RUN /bin/bash -c '. /.nvm/nvm.sh && nvm install stable'
RUN /bin/bash -c '. /.nvm/nvm.sh && nvm install v0.10.33 && nvm use v0.10.33 && nvm alias default v0.10.33 && ln -s /.nvm/v0.10.33/bin/node /usr/bin/node && ln -s /.nvm/v0.10.33/bin/npm /usr/bin/npm'

RUN npm install sitespeed.io -g

VOLUME /sitespeed.io

WORKDIR /sitespeed.io
