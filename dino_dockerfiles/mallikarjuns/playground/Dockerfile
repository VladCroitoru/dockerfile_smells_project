FROM ubuntu:latest
MAINTAINER MALLIK

RUN apt-get update
RUN apt-get install -y nodejs
RUN apt-get install -y npm
RUN ln -s /usr/bin/nodejs /usr/bin/node

RUN npm install -g http-server

ADD index.html /usr/apps/docker-playground/index.html
WORKDIR /usr/apps/docker-playground/

CMD ["http-server", "-s"]
