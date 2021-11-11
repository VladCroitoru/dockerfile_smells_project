#   Licensed to the Apache Software Foundation (ASF) under one or more
#   contributor license agreements.  See the NOTICE file distributed with
#   this work for additional information regarding copyright ownership.
#   The ASF licenses this file to You under the Apache License, Version 2.0
#   (the "License"); you may not use this file except in compliance with
#   the License.  You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.


FROM krallin/centos-tini:centos7
RUN yum install -y epel-release && yum install -y wget bash sed pwgen && yum clean all
RUN cd /opt/ && wget --no-cookies --no-check-certificate --header "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-cookie" "http://download.oracle.com/otn-pub/java/jdk/8u152-b16/aa0333dd3019491ca4f6ddbe78cdb6d0/jdk-8u152-linux-x64.tar.gz" && tar xzf jdk-8u152-linux-x64.tar.gz && rm -rf jdk-8u152-linux-x64.tar.gz

MAINTAINER David Skowronski <david@dskow.com>

# Config and data
ARG user=fuseki
ARG group=fuseki
ARG uid=1000
ARG gid=1000

ENV FUSEKI_BASE /var/fuseki_home
ENV FUSEKI_HOME /opt/fuseki

# Fuseki server is run with user `fuseki`, uid = 1510
# If you bind mount a volume from the host or a data container,
# ensure you use the same uid
RUN groupadd -g ${gid} ${group} \
	&& useradd -d "$FUSEKI_HOME" -u ${uid} -g ${gid} -m -s /bin/bash ${user}

# Update below according to https://jena.apache.org/download/
ARG FUSEKI_VERSION_MAJOR
ARG FUSEKI_VERSION_MINOR
ARG FUSEKI_VERSION_PATCH
ENV FUSEKI_VERSION=${SERVICEMIX_VERSION_MAJOR:-3}.${SERVICEMIX_VERSION_MINOR:-4}.${SERVICEMIX_VERSION_PATCH:-0}
ENV FUSEKI_MIRROR http://www-us.apache.org/dist/
ENV FUSEKI_ARCHIVE http://archive.apache.org/dist/ 
ENV JAVA_HOME /opt/jdk1.8.0_152
#

# fuseki.tar.gz checksum, download will be validated using it
ARG FUSEKI_SHA=0fe633fda08794ac88224b8c2c9cdea0b8baf4903d35594393e140348ce4466d


WORKDIR /tmp

# Download/check/unpack/move in one go (to reduce image size)
RUN     echo "$FUSEKI_SHA  fuseki.tar.gz" > fuseki.tar.gz.sha256 && \
		wget -O fuseki.tar.gz $FUSEKI_MIRROR/jena/binaries/apache-jena-fuseki-$FUSEKI_VERSION.tar.gz || \
        wget -O fuseki.tar.gz $FUSEKI_ARCHIVE/jena/binaries/apache-jena-fuseki-$FUSEKI_VERSION.tar.gz && \
        sha256sum -c fuseki.tar.gz.sha256 && \
        tar --directory=/opt -xzf /tmp/fuseki.tar.gz && \
		mv /opt/apache-jena-fuseki-${FUSEKI_VERSION}/* ${FUSEKI_HOME} && \
        rm fuseki.tar.gz* && \
		mkdir -p ${FUSEKI_BASE} && \
		chown "${user}":"${group}" ${FUSEKI_BASE} && \
		find ${FUSEKI_HOME}/. | xargs -i chown "${user}":"${group}" {}

# As "localhost" is often inaccessible within Docker container,
# we'll enable basic-auth with a random admin password
# (which we'll generate on start-up)
COPY docker-entrypoint.sh /
RUN chmod 755 /docker-entrypoint.sh

COPY shiro.ini /tmp/shiro.ini
COPY load.sh $FUSEKI_HOME
COPY tdbloader $FUSEKI_HOME
RUN chmod 755 $FUSEKI_HOME/load.sh $FUSEKI_HOME/tdbloader

# Where we start our server from
WORKDIR /opt/fuseki

USER ${user}

EXPOSE 3030
# Fuseki home directory is a volume, so configuration and fuseki data
# can be persisted and survive image upgrades
VOLUME $FUSEKI_BASE
ENTRYPOINT ["/usr/bin/tini", "--"]
CMD ["/docker-entrypoint.sh", "/opt/fuseki/fuseki-server"]
