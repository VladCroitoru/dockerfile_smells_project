FROM busybox
MAINTAINER Jonathan Dray <jonathan.dray@gmail.com>

# Create Cozy users, without home directories
# Set uid and gid based on other debian containers
RUN addgroup couchdb -g 109 \
&& adduser -H -S -u 105 -G couchdb couchdb \
&& mkdir -p /var/lib/couchdb \
&& chown couchdb:couchdb /var/lib/couchdb

VOLUME ["/var/lib/couchdb/"]
