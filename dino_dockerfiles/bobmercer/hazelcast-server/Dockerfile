FROM debian:jessie

MAINTAINER Damien Chambon <chambodn@skysoft-atm.com>
   
ENV HZ_VERSION 3.7.1
ENV HZ_HOME /opt/hazelcast/
ENV CLASSPATH ${HZ_HOME}/hazelcast-all-$HZ_VERSION.jar:$CLASSPATH/*:

# add our user and group first to make sure their IDs get assigned consistently, regardless of whatever dependencies get added
RUN groupadd -r hzgrp -g 433 && useradd -u 431 -r -m -g hzgrp -d /home/hzusr -s /bin/bash -c "Hazelcast Docker image user" hzusr

ENV GOSU_VERSION 1.9
RUN set -x \
    && apt-get update && apt-get install -y --no-install-recommends ca-certificates wget && rm -rf /var/lib/apt/lists/* \
    && dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')" \
    && wget -O /usr/local/bin/gosu "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch" \
    && wget -O /usr/local/bin/gosu.asc "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc" \
    && export GNUPGHOME="$(mktemp -d)" \
 	&& gpg --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4 \
    && gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \
    && rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \
    && chmod +x /usr/local/bin/gosu \
    && gosu nobody true \
    && apt-get purge -y --auto-remove ca-certificates wget

RUN set -x && \
	echo 'deb http://ftp.debian.org/debian jessie-backports main contrib' >> etc/apt/sources.list && \
	apt-get update && \
	apt-get install -y openjdk-8-jre wget supervisor curl vim inotify-tools && \
	apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
	mkdir -p ${HZ_HOME}/bin && \
	wget --quiet https://repo1.maven.org/maven2/com/hazelcast/hazelcast-all/${HZ_VERSION}/hazelcast-all-${HZ_VERSION}.jar -O ${HZ_HOME}/hazelcast-all-${HZ_VERSION}.jar

WORKDIR ${HZ_HOME}

COPY config/supervisor/supervisord.conf /etc/supervisor
COPY bin ${HZ_HOME}/bin
COPY docker-entrypoint.sh /

RUN chmod +x /docker-entrypoint.sh && \
	chmod +x ${HZ_HOME}/bin/start-node.sh

# Start hazelcast standalone server.
EXPOSE 5701 9001
ENTRYPOINT ["/bin/bash","/docker-entrypoint.sh"]
CMD ["hz-node"]