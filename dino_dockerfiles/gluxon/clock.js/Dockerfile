#
# fhsclock.js Dockerfile
#
# https://github.com/fhsav/clock.js
#

FROM dockerfile/nodejs
MAINTAINER Brandon Cheng

# Install MongoDB.
RUN \
  apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10 && \
  echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' > /etc/apt/sources.list.d/mongodb.list && \
  apt-get update && \
  apt-get install -y mongodb-org && \
  rm -rf /var/lib/apt/lists/*

# Define mountable directories.
VOLUME ["/data/db"]

# Define working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Install dependencies and copy app to working directory
ONBUILD COPY package.json /usr/src/app/
ONBUILD RUN npm install
ONBUILD COPY . /usr/src/app

# Define default command.
CMD ["npm", "start"]

EXPOSE 3000
