FROM ubuntu:latest
MAINTAINER Rhushikesh Saoji

RUN apt-get update
RUN apt-get install -y nodejs
RUN apt-get install -y npm
RUN ln -s /usr/bin/nodejs /usr/bin/node

RUN npm install -g http-server

ADD index.html /usr/apps/http/index.html
WORKDIR /usr/apps/http/

CMD ["http-server", "-s"]
