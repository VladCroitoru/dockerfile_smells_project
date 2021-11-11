FROM ubuntu:latest

LABEL description="NetSuite SDF CLI"
LABEL version="2017.2.0"

WORKDIR /opt/ns-cli 

ADD com.netsuite.ide.core_2017.2.0.jar .
ADD pom.xml .
ADD sdfcli .
ADD install-core.sh .

RUN apt update && apt install openjdk-8-jdk -y

ENV JAVA_HOME /usr/lib/jvm/java-1.8.0-openjdk-amd64
ENV PATH "$PATH:/opt/ns-cli"

RUN apt install maven -y
RUN sh /opt/ns-cli/install-core.sh
RUN mvn package

RUN apt install libxml2-utils -y && apt install curl -y && apt install zip -y && apt install git -y

CMD sh sdfcli -h 
