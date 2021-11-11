FROM java:8

MAINTAINER Mohammad Naghavi <mohamnag@gmail.com>

# Setup default environment, these have to be overwritten when running image
ENV AWS_ACCESS_KEY=NOTSET
ENV AWS_SECRET_KEY=NOTSET
ENV EC2_SEC_GROUP=NOTSET
ENV EC2_TAG_KEY=NOTSET
ENV EC2_TAG_VAL=NOTSET
ENV ORIENTDB_ROOT_PASSWORD=NOTSET
ENV HEAP_MEM_LIMIT=512M
ENV DISK_CACHE_BUFFER=1536
ENV ORIENTDB_NODE_NAME=NOTSET

# Default env params for backup, should be overwritten on running
ENV BACKUP_DB=NOTSET
ENV BACKUP_USER=NOTSET
ENV BACKUP_PASS=NOTSET


# Export internal variables
ENV ORIENTDB_HOME='/opt/orientdb'
ENV ORIENTDB_VERSION='2.1.11'
ENV BACKUP_DIR='/backups'
ENV ODB_NETWORK_LOCKTIMEOUT=30000
ENV ODB_NETWORK_SOCKETTIMEOUT=30000

# Install
RUN \
	curl -o orientdb.tar.gz http://orientdb.com/download.php?file=orientdb-community-${ORIENTDB_VERSION}.tar.gz && \
	mkdir -p ${ORIENTDB_HOME} && \
	tar -zxvf orientdb.tar.gz --strip-components=1 --directory ${ORIENTDB_HOME} && \
	rm -rf orientdb.tar.gz && \
	rm -rf ${ORIENTDB_HOME}/config \
	rm -rf ${ORIENTDB_HOME}/databases

# Add Configurations
ADD conf ${ORIENTDB_HOME}/config

# Add scripts
ADD scripts /opt/
RUN chmod +x /opt/service.sh
RUN chmod +x /opt/backup.sh

# Expose the necessary ports
EXPOSE 2424 2480 5701

# Escape union file system for DB & backup files
VOLUME ${ORIENTDB_HOME}/databases/
VOLUME ${BACKUP_DIR}

# Set the default command
CMD /opt/service.sh
