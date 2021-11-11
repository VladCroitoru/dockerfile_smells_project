#### Installation mongodb with auth and create user database
#FROM ubuntu:16.04
FROM mongo:latest
MAINTAINER gloriajun <pureainu@gmail.com>

# Import the public key used by the package management system
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927
# Create a list file for MongoDB
RUN echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.2.list

# update local package database
RUN apt-get update
# Install the latest stable version of MongoDB
RUN apt-get install -y mongodb-org

# create database folder
VOLUME ["/data/db"]

# excute mongodb
CMD ["mongod"]

# move script file for create db and user
ADD create_db.sh /create_db.sh

# expose ports
#   - 27017: process
#   - 28017: http
EXPOSE 27017
EXPOSE 28017
