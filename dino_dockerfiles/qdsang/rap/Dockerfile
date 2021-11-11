FROM haraldkoch/alpine-tomcat7:latest

MAINTAINER qdsang <qdsang@gmail.com>

RUN rm -rf /usr/tomcat/webapps/docs /usr/tomcat/webapps/examples /usr/tomcat/webapps/ROOT
#ADD ./RAP-0.14.1-SNAPSHOT.war /usr/tomcat/webapps/ROOT.war
ADD http://rap.taobao.org/release/RAP-0.14.1-SNAPSHOT.war /usr/tomcat/webapps/ROOT.war

ADD ./run.sh /usr/local/bin/run

EXPOSE 8080




