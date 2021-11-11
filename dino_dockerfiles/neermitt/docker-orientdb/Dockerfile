############################################################
# Dockerfile to run an OrientDB (Graph) Container
############################################################

FROM java:8

MAINTAINER Neeraj Mittal <mittal.neeraj@gmail.com>

ENV ORIENTDB_VERSION 2.2.0-beta
ENV ORIENTDB_DOWNLOAD_MD5 a1b6abe1f0c45312be0a1a0831525386
ENV ORIENTDB_DOWNLOAD_SHA1 ac265bb16a55a62066b5403fd6f3cd94333db8df

#download distribution tar, untar and delete databases
RUN mkdir /orientdb && \
wget  "http://central.maven.org/maven2/com/orientechnologies/orientdb-community/$ORIENTDB_VERSION/orientdb-community-$ORIENTDB_VERSION.tar.gz" \
&& echo "$ORIENTDB_DOWNLOAD_MD5 *orientdb-community-$ORIENTDB_VERSION.tar.gz" | md5sum -c - \
&& echo "$ORIENTDB_DOWNLOAD_SHA1 *orientdb-community-$ORIENTDB_VERSION.tar.gz" | sha1sum -c - \
&& tar -xvzf orientdb-community-$ORIENTDB_VERSION.tar.gz -C /orientdb --strip-components=1\
&& rm orientdb-community-$ORIENTDB_VERSION.tar.gz \
&& rm -rf /orientdb/databases/*


ENV PATH /orientdb/bin:$PATH

VOLUME ["/orientdb/backup", "/orientdb/databases", "/orientdb/config"]

WORKDIR /orientdb

#OrientDb binary
EXPOSE 2424

#OrientDb http
EXPOSE 2480

#OrientDb hazelcast cluster
EXPOSE 5701

# Default command start the server
CMD ["server.sh"]