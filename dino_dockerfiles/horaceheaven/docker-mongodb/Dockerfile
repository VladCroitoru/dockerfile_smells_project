FROM ubuntu:latest
MAINTAINER Horace Heaven "hheaven@medullan.com"

# Import MongoDB public GPG key AND create a MongoDB list file
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10

RUN echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' | tee /etc/apt/sources.list.d/10gen.list

# Update software packages
RUN apt-get -y update

# Install mongodb
RUN apt-get install -y -q mongodb-org

# Create the MongoDB data directory
RUN mkdir -p /data/db

# Expose port 27017 from the container to the host
EXPOSE 27017

ENTRYPOINT usr/bin/mongod
