FROM node:latest

MAINTAINER leijun.yang@nio.com

ENV DEBIAN_FRONTEND noninteractive

RUN \
apt-get update && \
apt-get -y --no-install-recommends install wget curl && \
npm install -g pouchdb-server && \
apt-get -y autoremove && \
apt-get -y autoclean

ADD add-db-user.sh /usr/bin/add-db-user.sh
RUN chmod +x /usr/bin/add-db-user.sh

RUN mkdir /pouchdb

WORKDIR /pouchdb

EXPOSE 5984

CMD ["pouchdb-server", "-p", "5984", "-o", "0.0.0.0"]
