FROM weboaks/node-karma-protractor-chrome:latest

ENV AWS_CLI_VERSION 1.11.131

WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y \
     python3 python3-pip libgconf-2-4 && \
     pip3 install awscli==${AWS_CLI_VERSION}
