FROM debian:latest
MAINTAINER Rony Dray <contact@obigroup.fr>, Jonathan Dray <jonathan.dray@gmail.com>

RUN echo 'deb http://http.debian.net/debian wheezy main contrib non-free' >> /etc/apt/sources.list
RUN apt-get -y update
RUN apt-get install -y \
    g++ \
    couchdb \
    python-pip \
    wget \
    curl \
    && apt-get clean

# Clean APT cache for a lighter image
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN pip install supervisor

# Create Cozy users, without home directories.
RUN useradd -M cozy \
&& useradd -M cozy-data-system

# Copy couch db configuration file for cozy cloud
ADD couchdb/cozy.ini /etc/couchdb/local.d/cozy.ini

# Generate a random login and password for couchdb
RUN mkdir /etc/cozy \
&& chown -hR cozy /etc/cozy \
&& COUCH_LOGIN=`< /dev/urandom tr -dc _A-Z-a-z-0-9 | head -c${1:-32}`; \
echo $COUCH_LOGIN > /etc/cozy/couchdb.login \
&& sed -ir "s/<login>/${COUCH_LOGIN}/g" /etc/couchdb/local.d/cozy.ini \
&& COUCH_PASSWD=`< /dev/urandom tr -dc _A-Z-a-z-0-9 | head -c${1:-32}`; \
echo $COUCH_PASSWD >> /etc/cozy/couchdb.login \
&& sed -ir "s/<pwd>/${COUCH_PASSWD}/g" /etc/couchdb/local.d/cozy.ini \
&& chown couchdb /etc/couchdb/local.d/cozy.ini \
&& chmod 640 /etc/cozy/couchdb.login \
&& mkdir /var/run/couchdb \
&& chown -hR couchdb /var/run/couchdb

# Configure Supervisor.
ADD supervisor/supervisord.conf /etc/supervisord.conf
RUN mkdir -p /var/log/supervisor \
&& chmod 774 /var/log/supervisor \
&& /usr/local/bin/supervisord -c /etc/supervisord.conf

# Import Supervisor configuration files.
ADD supervisor/couchdb.conf /etc/supervisor/conf.d/couchdb.conf
RUN chmod 0644 /etc/supervisor/conf.d/*

#Add file for backup/restore
ADD sh/backup.sh /home/backup.sh
ADD sh/restore.sh /home/restore.sh

# Expose couch port to make it easier for other docker containers
EXPOSE 5984

# # Default user when running the container
# USER couchdb

VOLUME ["/etc/cozy", "/var/lib/couchdb/"]

# Setting config dir to couch main directory
WORKDIR /var/lib/couchdb

CMD [ "/usr/local/bin/supervisord", "-n", "-c", "/etc/supervisord.conf" ]