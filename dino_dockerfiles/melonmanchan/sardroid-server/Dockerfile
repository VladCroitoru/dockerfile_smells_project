FROM ubuntu:14.04
MAINTAINER Matti Jokitulppo <matti.jokitulppo@aalto.fi>

RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list
RUN apt-get update
RUN apt-get upgrade -y

RUN apt-get install -y curl git
RUN curl -sL https://deb.nodesource.com/setup_5.x | sudo -E bash -

RUN apt-get install -y nodejs

RUN npm install -g babel-cli

RUN npm install -g sequelize-cli

RUN mkdir /sardroid

ADD . /sardroid

WORKDIR /sardroid

RUN chmod +x /sardroid/scripts/start-server.sh

EXPOSE 9000

CMD ["bash", "/sardroid/scripts/start-server.sh"]

