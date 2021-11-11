# Need a debian sid for now to get decent version of couchdb
FROM debian:sid
MAINTAINER Rony Dray <contact@obigroup.fr>, Jonathan Dray <jonathan.dray@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

# Add debian stable repository to apt source list
# This is required to be able to fetch all couchdb dependencies
RUN echo "deb http://httpredir.debian.org/debian/ stable main" > /etc/apt/sources.list.d/debian-stable.list

RUN apt-get -y update && apt-get install --quiet --assume-yes --no-install-recommends \
    couchdb \
    && apt-get clean

# Clean APT cache for a lighter image
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Create Cozy users, without home directories
# Create user early to avoid uid / gid issues
RUN useradd -M cozy

# Generate a random login and password for couchdb
RUN mkdir /var/run/couchdb \
&& chown -hR couchdb /var/run/couchdb

# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/couchdb/couchdb.log

# Expose couch port to make it easier for other docker containers
EXPOSE 5984

VOLUME ["/var/lib/couchdb/"]

# Setting config dir to couch main directory
WORKDIR /var/lib/couchdb

# Default user when running the container
USER couchdb
CMD ["/usr/bin/couchdb"]
