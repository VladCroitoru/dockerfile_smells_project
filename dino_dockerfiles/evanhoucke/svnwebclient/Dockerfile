FROM tomcat:7-jre7-alpine

ENV SVNWEB_VERSION=3.1.0

RUN apk update &&\
    apk upgrade &&\
    apk add unzip &&\
    apk add wget

RUN wget http://community.polarion.com/projects/svnwebclient/download/svnwebclient-${SVNWEB_VERSION}.zip &&\
    rm -rf /usr/local/tomcat/webapps/ROOT &&\
    mkdir /usr/local/tomcat/webapps/ROOT &&\
    unzip svnwebclient-${SVNWEB_VERSION}.zip svnwebclient.war -d /usr/local/tomcat/webapps/ROOT &&\
    unzip /usr/local/tomcat/webapps/ROOT/svnwebclient.war -d /usr/local/tomcat/webapps/ROOT &&\
    rm /usr/local/tomcat/webapps/ROOT/svnwebclient.war

