FROM tomcat:8.5.5-jre8-alpine

ENV RAP_VERSION 0.14.1

RUN wget  -O RAP.war http://rap.taobao.org/release/RAP-${RAP_VERSION}-SNAPSHOT.war \
    && rm -rf /usr/local/tomcat/webapps/ROOT/* \
    && unzip -x RAP.war -d /usr/local/tomcat/webapps/ROOT \
    && rm -rf RAP.war

COPY config.properties /usr/local/tomcat/webapps/ROOT/WEB-INF/classes/config.properties
