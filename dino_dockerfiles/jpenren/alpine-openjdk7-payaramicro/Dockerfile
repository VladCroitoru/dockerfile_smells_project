FROM jpenren/alpine-openjdk7

MAINTAINER Javier Pena

ENV VERSION 4.1.1.162

RUN mkdir -p /opt/payara-micro/webapps &&\
    wget -P /opt/payara-micro/ http://s3-eu-west-1.amazonaws.com/payara.co/Payara+Downloads/Payara+$VERSION/payara-micro-$VERSION.jar

EXPOSE 8080

ENTRYPOINT java -jar /opt/payara-micro/payara-micro-$VERSION.jar --deploymentDir /opt/payara-micro/webapps
