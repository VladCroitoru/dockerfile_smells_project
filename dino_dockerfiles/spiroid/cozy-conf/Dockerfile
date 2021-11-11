FROM busybox
MAINTAINER Jonathan Dray <jonathan.dray@gmail.com>

ADD cozy.ini /etc/couchdb/local.d/cozy.ini

# Create Cozy users, without home directories
# Set uid and gid based on other debian containers
RUN addgroup couchdb -g 109 \
&& adduser -H -S -u 105 -G couchdb couchdb

# Generate a random login and password for couchdb
RUN mkdir /etc/cozy \
&& mkdir -p /etc/couchdb/local.d \
&& chown -hR default /etc/cozy \
&& COUCH_LOGIN=`< /dev/urandom tr -dc _A-Z-a-z-0-9 | head -c${1:-32}`; \
echo $COUCH_LOGIN > /etc/cozy/couchdb.login \
&& sed -ir "s/<login>/${COUCH_LOGIN}/g" /etc/couchdb/local.d/cozy.ini \
&& COUCH_PASSWD=`< /dev/urandom tr -dc _A-Z-a-z-0-9 | head -c${1:-32}`; \
echo $COUCH_PASSWD >> /etc/cozy/couchdb.login \
&& sed -ir "s/<pwd>/${COUCH_PASSWD}/g" /etc/couchdb/local.d/cozy.ini \
&& chown couchdb /etc/couchdb/local.d/cozy.ini \
&& chmod 640 /etc/cozy/couchdb.login

VOLUME ["/etc/couchdb/local.d", "/etc/cozy"]
