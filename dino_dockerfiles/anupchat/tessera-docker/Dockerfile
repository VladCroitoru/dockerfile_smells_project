# Tessera Dockerfile
#
# https://github.com/anupchat/tessera-docker
#
# VERSION 1.0
# Gets a Node and NPM container using precise ubuntu base.

FROM nodesource/node:precise
MAINTAINER Anup Chatterjee <anup.chat@gmail.com>

# If you are behind a proxy
#ENV http_proxy http://www-proxy.us.com:80
#ENV https_proxy http://www-proxy.us.com:80
# Prepare
RUN apt-get update

# Install base package dependencies
RUN apt-get install -y python-pip python-dev python-software-properties wget curl ca-certificates git

# Install dependencies for tessera
RUN npm install -g grunt-cli

# Deploy tessera
RUN git clone https://github.com/urbanairship/tessera.git /tessera
WORKDIR /tessera

RUN pip install -r requirements.txt
RUN pip install -r dev-requirements.txt
RUN npm install
RUN grunt

RUN invoke initdb
# This is if you need the demo dashboards. Note that there were errors running this.
#RUN invoke json.import 'demo/*'

EXPOSE 5000
CMD invoke run