FROM ubuntu:14.04

# Install RethinkDB.

RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get -y install curl
RUN echo "deb http://download.rethinkdb.com/apt trusty main" | sudo tee /etc/apt/sources.list.d/rethinkdb.list
RUN curl -s http://download.rethinkdb.com/apt/pubkey.gpg | apt-key add -
RUN apt-get update
RUN apt-get -y install rethinkdb=1.13.3-0ubuntu1~trusty

# Define mountable directories.
VOLUME ["/data"]

# Define working directory.
WORKDIR /data

# Define default command.
CMD ["rethinkdb", "--bind", "all"]

# Expose ports.
#   - 8080: web UI
#   - 28015: process
#   - 29015: cluster
EXPOSE 8080
EXPOSE 28015
EXPOSE 29015
