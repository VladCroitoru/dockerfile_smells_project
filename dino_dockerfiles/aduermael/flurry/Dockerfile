# Pull base image.
FROM ubuntu:13.04

RUN apt-get install -y wget

# Install Node.js
RUN wget http://nodejs.org/dist/v0.10.26/node-v0.10.26-linux-x64.tar.gz
RUN tar -zxvf node-v0.10.26-linux-x64.tar.gz

RUN cd node-v0.10.26-linux-x64; cp -R bin/* /usr/local/bin; cp -R lib/* /usr/local/lib; cp -R share/* /usr/local/share; cp -R include/* /usr/local/include

RUN rm -r node-v0.10.26-linux-x64
RUN rm node-v0.10.26-linux-x64.tar.gz

ADD srv /srv

RUN cd /srv; npm install;

RUN npm install forever -g;

# install redis
RUN apt-get update -y
RUN apt-get install redis-server -y

EXPOSE 80

ENV HOME /root
WORKDIR /srv

# Define default command.
CMD ["/bin/bash","/srv/start.sh"]

