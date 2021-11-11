FROM ubuntu:latest
MAINTAINER Sandip
RUN apt-get update
RUN apt-get install -y nodejs
RUN apt-get install -y npm
RUN npm install -g http-server
RUN ln -s /usr/bin/nodejs /usr/bin/node
ADD index.html /usr/apps/hello-docker/index.html
WORKDIR /usr/apps/hello-docker/
CMD ["http-server", "-s"] 
