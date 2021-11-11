FROM node:latest
MAINTAINER Oriol Boan <dev@orboan.com>
LABEL Vendor="node.js"
LABEL License=GPLv2

RUN apt-get -y update && apt-get clean all \
&& apt-get install libcurl4-gnutls-dev libexpat1-dev gettext \
libz-dev libssl-dev -y \
&& apt-get install git-all -y \
&& apt-get install -y markdown

RUN apt-get install -y vim && apt-get install -y nano 

RUN npm install -g javascripting \
&& npm install -g learnyounode \
&& npm install -g git-it \
&& npm install -g how-to-markdown \
&& npm install -g how-to-npm \
&& npm install -g stream-adventure \
&& npm install -g scope-chains-closures \
&& npm install -g elementary-electron \
&& npm install -g functional-javascript-workshop \
&& npm install -g levelmeup \
&& npm install -g expressworks \
&& npm install -g async-you \
&& npm install -g regex-adventure \
&& npm install -g learn-sass \
&& npm install -g learnyoucouchdb \
&& npm install -g learnyoumongo \
&& npm install -g learnyoubash \
&& npm install -g less-is-more \
&& npm install -g bytewiser

RUN echo 'alias ls="ls --color"' >> ~/.bashrc \
&& echo 'alias ll="ls -lh"' >> ~/.bashrc \
&& echo 'alias la="ls -lha"' >> ~/.bashrc

VOLUME /nodeschool
WORKDIR /nodeschool
EXPOSE 80

ENTRYPOINT ["/bin/bash"]

