FROM ubuntu:20.04
LABEL maintainer="dalmatialab"

# Install tzdata and set right timezone
ENV DEBIAN_FRONTEND="noninteractive"
RUN apt update && apt-get -y install tzdata
ENV TZ=Europe/Zagreb

# Environment setup
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/
ENV GEOMESA_VERSION=3.1.0
ENV SCALA_VERSION=2.11

# Java installation
RUN apt-get update && apt-get install -y openjdk-8-jdk wget

# Maven installation
RUN apt-get update && apt-get install -y maven git

# Scala installation
RUN apt-get update && apt-get install wget && wget www.scala-lang.org/files/archive/scala-2.11.12.deb && dpkg -i scala-2.11.12.deb && rm scala-2.11.12.deb

RUN mkdir -p /jars/
RUN mkdir -p /build/geomesa
RUN cd /build/geomesa/ && git clone https://github.com/geomesa/geomesa-tutorials.git . &&  git checkout geomesa-tutorials-${GEOMESA_VERSION} && mvn clean install -pl geomesa-tutorials-accumulo/geomesa-tutorials-accumulo-quickstart -am && cp geomesa-tutorials-accumulo/geomesa-tutorials-accumulo-quickstart/target/geomesa-tutorials-accumulo-quickstart-${GEOMESA_VERSION}.jar /jars/
RUN cd /jars && wget https://repo1.maven.org/maven2/org/eclipse/paho/org.eclipse.paho.client.mqttv3/1.2.5/org.eclipse.paho.client.mqttv3-1.2.5.jar
RUN wget -P /jars/ https://repo1.maven.org/maven2/com/lihaoyi/ujson_2.11/0.6.5/ujson_2.11-0.6.5.jar

RUN mkdir importer
ADD ./src/ /importer
WORKDIR /importer/

RUN chmod a+x /importer/run.sh

CMD ["sh","-c","/importer/run.sh"]