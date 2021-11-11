FROM ubuntu:latest
MAINTAINER Chrstian Heimke

RUN sudo apt-get update 
RUN sudo apt-get install -y openjdk-7-jre-headless openjdk-7-jre

WORKDIR /usr/src

ADD http://meteorite.bi/downloads/saiku-server-3.0.7.tar.gz /usr/src/saiku-server-3.0.7.tar.gz
RUN tar xvfz saiku-server-3.0.7.tar.gz

EXPOSE 8080

CMD /usr/src/saiku-server/start-saiku.sh && tail -f /usr/src/saiku-server/tomcat/logs/catalina.out