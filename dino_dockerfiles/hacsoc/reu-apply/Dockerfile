FROM node:4-onbuild
MAINTAINER Philip Smith <pas147@case.edu>
# Node running port
EXPOSE 3000
# Mongo running port
EXPOSE 27017
# IMport mongodb public key and make list file
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927
RUN echo "deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.2 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.2.list
# apt-get sources and install mongo
RUN apt-get update
RUN apt-get install -y apt-utils
RUN apt-get upgrade -y
RUN apt-get install -y mongodb
# make data directory
RUN mkdir -p /data/db
# entry point for mongo
ENTRYPOINT ["/usr/bin/mongod"]