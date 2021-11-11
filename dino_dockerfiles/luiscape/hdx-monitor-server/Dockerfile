############################################################
# Dockerfile to build the HDX Monitor Server application
# Based on Node. Receives links from a MongoDB container.
############################################################

FROM node:latest

MAINTAINER Luis Capelo <capelo@un.org>

#
# Clone and install dependencies.
#
RUN \
  npm install -g pm2 \
  && git clone https://github.com/luiscape/hdx-monitor-server \
  && cd hdx-monitor-server \
  && npm install

#
# Install the MongoDB shell
# for configuring the database.
#
RUN \
  apt-key adv --keyserver keyserver.ubuntu.com --recv 7F0CEB10 \
  && echo "deb http://repo.mongodb.org/apt/debian wheezy/mongodb-org/3.0 main" | tee /etc/apt/sources.list.d/mongodb-org-3.0.list \
  && apt-get update \
  && apt-get install -y mongodb-org-shell


WORKDIR "/hdx-monitor-server"

EXPOSE 8080

CMD ["make", "run"]
