FROM ubuntu:14.04

RUN apt-get update \
	&& apt-get install -y --no-install-recommends sudo iptables unzip curl wget git-core software-properties-common \
	&& update-ca-certificates \
	&& rm -rf /var/lib/apt/lists/*

# amazon correcto openjdk8 since Java SDK 8 PPA is discontinued.
RUN wget https://d3pxv6yz143wms.cloudfront.net/8.212.04.2/java-1.8.0-amazon-corretto-jdk_8.212.04-2_amd64.deb && \
    apt-get update &&  apt-get install java-common && apt-get install -y --no-install-recommends apt-utils && \
    dpkg --install java-1.8.0-amazon-corretto-jdk_8.212.04-2_amd64.deb

# Get and install teamcity
ENV TEAMCITY_VERSION 2021.1.2
ENV TEAMCITY_DATA_PATH /var/lib/teamcity

RUN wget -qO- https://download.jetbrains.com/teamcity/TeamCity-$TEAMCITY_VERSION.tar.gz | tar xz -C /opt \
  && mkdir -p $TEAMCITY_DATA_PATH/config

# Enable the correct Valve when running behind a proxy
RUN sed -i -e "s/\.*<\/Host>.*$/<Valve className=\"org.apache.catalina.valves.RemoteIpValve\" protocolHeader=\"x-forwarded-proto\" \/><\/Host>/" /opt/TeamCity/conf/server.xml

# Entrypoint
COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]

EXPOSE 8111
VOLUME /var/lib/teamcity
