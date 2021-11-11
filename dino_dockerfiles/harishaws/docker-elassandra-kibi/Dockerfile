FROM debian:latest

# Maintainer
MAINTAINER lmangani <lorenzo.mangani@gmail.com>

# Setup
RUN \
 export DEBIAN_FRONTEND=noninteractive \
 && echo "deb     http://mirror.steadfast.net/debian/ testing main contrib non-free" >> /etc/apt/sources.list.d/testing.list \
 && echo "deb     http://ftp.us.debian.org/debian/    testing main contrib non-free" >> /etc/apt/sources.list.d/testing.list \
 && echo "deb http://packages.elassandra.io/deb/ ./" >> /etc/apt/sources.list.d/elassandra.list \
 && apt-get update && apt-get install -y wget unzip \
 && wget -O- -q http://packages.elassandra.io/pub/GPG-KEY-Elassandra > /tmp/GPG-KEY-Elassandra \
 && apt-key add  /tmp/GPG-KEY-Elassandra \
 # Setup pip packages
 && apt-get -y install python-pip python-cassandra wget curl libjemalloc1 \
 && pip install --upgrade pip \
 && pip install --upgrade cassandra-driver \
 && pip install cqlsh \
 ## Install Java
 && apt-get -y --force-yes install oracle-java8-jre \
 && update-alternatives --auto java \
 ## Install JNA
 && apt-get -y install libjna-java \
 # && ln -s /usr/share/java/jna.jar /usr/share/cassandra/lib \
 ## Install Elassandra 
 && wget -O /tmp/elassandra-242-snap.zip https://transfer.sh/scQHP/elassandra-2.4.2.zip \
 && unzip /tmp/elassandra-242-snap.zip -d /opt && mv /opt/elassandra-2.4.2 /opt/elassandra \
 && rm -rf /tmp/elassandra-242-snap.zip \
 # && apt-get clean && apt-get -y --force-yes install elassandra \
 ## Setup Extras
 && groupadd -r kibi && useradd -r -m -g kibi kibi \
 && wget -O /dumb-init https://github.com/Yelp/dumb-init/releases/download/v1.1.3/dumb-init_1.1.3_amd64 \
 && chmod +x /dumb-init \
 && curl -sL https://deb.nodesource.com/setup_4.x | bash - \
 && apt-get install -y nodejs \
 ## Get Kibi
 && cd /opt && wget https://download.support.siren.solutions/kibi/community?file=kibi-community-standalone-4.5.4-linux-x64.zip -O kibi-4.5.4-linux-x64.zip \
 && unzip kibi-4.5.4-linux-x64.zip \
 && rm -rf /opt/kibi-4.5.4-linux-x64.zip \
 && mv kibi-community-standalone-4.5.4-linux-x64 kibi \
 && chown -R kibi:kibi /opt/kibi \
 ## Stuff
 && cd /opt/kibi \
 && ./bin/kibi plugin --install sentinl -u https://github.com/sirensolutions/sentinl/releases/download/snapshot/sentinl-latest.tar.gz \
 # && ./bin/kibi plugin --install kibana-auth-plugin -u https://github.com/elasticfence/kibana-auth-elasticfence/releases/download/snapshot/kauth-latest.tar.gz \
 && ./bin/kibi plugin --install kibrand -u https://github.com/elasticfence/kibrand/archive/0.4.5.zip \
 && ./bin/kibi plugin --install elastic/timelion \
 && ./bin/kibi plugin --install elastic/sense \
 && chown -R kibi:kibi /opt/kibi \
 && chown -R kibi:kibi /opt/elassandra \
 ## Reverse Proxy
 && npm install -g kiss-proxy \
 ## Swapoff attempt
 && swapoff -a \
 ## Cleanup
 && apt-get autoremove && apt-get clean \
 && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY entrypoint.sh /opt/
RUN chmod 755 /opt/entrypoint.sh

COPY runas.sh /opt/
RUN chmod 755 /opt/runas.sh

EXPOSE 7000/tcp 7001/tcp 7199/tcp 9042/tcp 9160/tcp 9200/tcp 9222/tcp 5601/tcp 5606/tcp

# Exec on start
ENTRYPOINT ["/dumb-init", "--"]
CMD ["/opt/runas.sh"]
