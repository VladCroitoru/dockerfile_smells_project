FROM ubuntu:14.04

MAINTAINER Chai Phonbopit

RUN sudo apt-get update && sudo apt-get -y upgrade && \
    sudo apt-get install -y build-essential git curl && \
    curl -sL https://deb.nodesource.com/setup_4.x | sudo -E bash - && \
    sudo apt-get install -y nodejs

RUN mkdir /var/www/ && mkdir /var/www/node-app
ADD ./app /var/www/node-app

WORKDIR /var/www/node-app
RUN npm install
EXPOSE 7777
CMD ["npm", "start"]
