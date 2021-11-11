# Use Ubuntu
FROM ubuntu:latest

MAINTAINER PrankurK

# Install wger & JRE
RUN apt-get clean && \
        apt-get update && \
        apt-get -qy install \
		                        wget \
                                openjdk-8-jdk \
								curl \
                                unzip

RUN   mkdir -p /maven
RUN   mkdir -p /project

#Install Influxdb
RUN set -ex && \
    for key in \
        05CE15085FC09D18E99EFB22684A14CF2582E0C5 ; \
    do \
        gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key" || \
        gpg --keyserver pgp.mit.edu --recv-keys "$key" || \
        gpg --keyserver keyserver.pgp.com --recv-keys "$key" ; \
    done

ENV INFLUXDB_VERSION 1.2.4
RUN wget -q https://dl.influxdata.com/influxdb/releases/influxdb_${INFLUXDB_VERSION}_amd64.deb.asc && \
    wget -q https://dl.influxdata.com/influxdb/releases/influxdb_${INFLUXDB_VERSION}_amd64.deb && \
    gpg --batch --verify influxdb_${INFLUXDB_VERSION}_amd64.deb.asc influxdb_${INFLUXDB_VERSION}_amd64.deb && \
    dpkg -i influxdb_${INFLUXDB_VERSION}_amd64.deb && \
    rm -f influxdb_${INFLUXDB_VERSION}_amd64.deb*
#COPY influxdb.conf /etc/influxdb/influxdb.conf

EXPOSE 8086

VOLUME /var/lib/influxdb

#COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
CMD ["influxd"]
			
#Install MVN
ARG MAVEN_VERSION=3.5.0
ARG USER_HOME_DIR="/maven"
ARG BASE_URL=https://apache.osuosl.org/maven/maven-3/${MAVEN_VERSION}/binaries

#RUN mkdir -p /usr/share/maven /usr/share/maven/ref \
RUN mkdir -p -m 777 /maven \
  && curl -fsSL -o /tmp/apache-maven.tar.gz ${BASE_URL}/apache-maven-$MAVEN_VERSION-bin.tar.gz \
  && tar -xzf /tmp/apache-maven.tar.gz -C /maven --strip-components=1 \
  && rm -f /tmp/apache-maven.tar.gz \
  && ln -s /maven/bin/mvn /usr/bin/mvn

ENV MAVEN_HOME /maven/bin
ENV MAVEN_CONFIG "$USER_HOME_DIR/.m2"
VOLUME "$USER_HOME_DIR/.m2"
