# DOCKER-VERSION 0.10.0

# Pull base image.
FROM ubuntu:14.04

# Install Node.js
RUN apt-get update
RUN apt-get install -y software-properties-common
RUN add-apt-repository -y ppa:chris-lea/node.js
RUN apt-get update
RUN apt-get install -y nodejs

ADD . /src

RUN cd /src; npm install

EXPOSE 3001

CMD ["node", "/src/web.js"]
