FROM ubuntu:18.04
ENV BUILD_DATE=04_Novenber_2019
ENV TERM=xterm
RUN apt-get update
RUN apt-get install -y software-properties-common curl sudo

RUN curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -
RUN apt-get install -y nodejs git git-core gcc make build-essential

RUN npm install -g jest typescript@3.8.3
RUN npm i -g  https://github.com/terbooter/bitbucket-pipelines-helper.git