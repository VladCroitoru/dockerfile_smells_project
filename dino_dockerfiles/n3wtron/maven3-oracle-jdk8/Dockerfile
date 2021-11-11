FROM frolvlad/alpine-oraclejdk8

ENV MAVEN_HOME /opt/maven

ENV PATH $PATH:$MAVEN_HOME/bin

RUN apk add --no-cache wget curl

RUN cd /tmp \
	&& wget -nv http://it.apache.contactlab.it/maven/maven-3/3.3.9/binaries/apache-maven-3.3.9-bin.tar.gz \
	&& tar xzvf apache-maven-3.3.9-bin.tar.gz \
	&& mkdir /opt \
	&& mv /tmp/apache-maven-3.3.9 $MAVEN_HOME \
	&& rm /tmp/apache-maven-3.3.9-bin.tar.gz

VOLUME /root/.m2
