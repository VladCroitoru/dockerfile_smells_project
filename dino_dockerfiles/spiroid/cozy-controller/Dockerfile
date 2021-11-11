FROM node:4.5
MAINTAINER Rony Dray <contact@obigroup.fr>, Jonathan Dray <jonathan.dray@gmail.com>

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update \
&&  apt-get install --quiet --assume-yes --no-install-recommends \
      build-essential \
      curl \
      imagemagick \
      libffi-dev \
      nano \
      python-dev \
      sqlite3 \
      sudo \
&&  apt-get clean \
&&  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install CoffeeScript & Cozy Controller
RUN npm install -g \
    coffee-script \
    cozy-controller \
    cozy-monitor

# Create Cozy users, without home directories.
RUN useradd -M cozy \
&&  useradd -M cozy-data-system \
&&  useradd -M cozy-home

# Need ENV VARS:
ENV NODE_ENV=production \
	COUCH_HOST=couchdb \
	COUCH_PORT=5984

# Expose port
EXPOSE 9002 9104

VOLUME ["/usr/local/cozy/", "/usr/local/var/log/cozy"]

ADD init.sh /usr/local/bin/cozy-init.sh

WORKDIR /usr/local/lib/node_modules/cozy-controller/build/

CMD [ "node", "server.js" ]
