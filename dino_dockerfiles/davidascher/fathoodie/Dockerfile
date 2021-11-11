FROM ubuntu
MAINTAINER David Ascher <david.ascher@gmail.com>
 
# Get us to a stable place
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y python-software-properties
 
RUN apt-get remove couchdb
 
# CouchDB dependencies
## get developer tools dependencies
RUN apt-get install -y g++ make
RUN apt-get install -y xdg-utils
RUN apt-get install -y erlang-dev erlang-manpages erlang-base-hipe erlang-eunit erlang-nox erlang-xmerl erlang-inets
 
### couchdb developer dependencies
RUN apt-get install -y libmozjs185-dev libicu-dev libcurl4-gnutls-dev libtool
 
### unpack source
RUN apt-get install -y wget curl git
RUN cd /tmp && wget http://mirror.csclub.uwaterloo.ca/apache/couchdb/source/1.4.0/apache-couchdb-1.4.0.tar.gz && tar xvzf apache-couchdb-1.4.0.tar.gz
RUN cd /tmp/apache-couchdb-1.4.0 && ./configure && make && make install
 
### install logrotate and initd scripts
RUN ln -s /usr/local/etc/logrotate.d/couchdb /etc/logrotate.d/couchdb
RUN ln -s /usr/local/etc/init.d/couchdb /etc/init.d
 
# node
RUN add-apt-repository ppa:chris-lea/node.js
RUN apt-get update -y
RUN apt-get install -y nodejs
RUN npm install -g hoodie-cli
 
# Alt dependencies
 
EXPOSE 6001 6002 
 
# this avoids asking for couch admin pw
ENV CI true
# this avoid hoodie only accepting connections from localhost (kinda pointless in a docker world)
ENV HOODIE_BIND_ADDRESS 0.0.0.0
RUN hoodie new theapp
WORKDIR theapp
RUN npm install
CMD hoodie start -n
