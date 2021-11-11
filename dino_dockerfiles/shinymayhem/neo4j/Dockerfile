FROM shinymayhem/base

ENV neohome /usr/local/neo4j-server
ENV neolib /var/lib/neo4j-server

RUN \
	apt-get install -y software-properties-common lsof && \
	echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
	add-apt-repository -y ppa:webupd8team/java && \
	apt-get update && \
	apt-get install -y oracle-java7-installer && \
	rm -rf /var/lib/apt/lists/* && \
	rm -rf /var/cache/oracle-jdk7-installer && \
	cd /tmp && \
	wget http://neo4j.com/artifact.php?name=neo4j-community-2.1.6-unix.tar.gz -O neo4j.tar.gz && \
	useradd neo4j -m -d ${neohome} && \
	cd /tmp && \
	mkdir neo4j && \
	tar -zxf neo4j.tar.gz -C ./ && \
	rm neo4j.tar.gz && \
	mv neo4j-community-2.1.6/* ${neohome} && \
	ln -s ${neohome}/bin/neo4j /usr/local/bin/neo4j && \
	mkdir ${neolib} && \
	chown -R neo4j:neo4j ${neohome} && \
	chown -R neo4j:neo4j ${neolib}

VOLUME ${neolib}

ADD etc/init.d/neo4j /etc/init.d/neo4j
ADD conf/neo4j-server.properties ${neohome}/conf/neo4j-server.properties
ADD conf/neo4j.properties ${neohome}/conf/neo4j.properties
ADD conf/neo4j-wrapper.conf ${neohome}/conf/neo4j-wrapper.conf
ADD conf/neo4j.conf /etc/security/limits.d/neo4j.conf

RUN chmod +x /etc/init.d/neo4j

USER neo4j

EXPOSE 7474
#run in foreground
CMD neo4j console
