#FROM openjdk:8-jdk 
FROM openjdk:10-jdk
MAINTAINER LogicalDOC <packagers@logicaldoc.com>

ENV CATALINA_HOME /usr/local/logicaldoc/tomcat
ENV TOMCAT_VERSION 8.5.31
ENV TERM xterm

# Add needed convert tools 
RUN apt-get update && apt-get install -y --no-install-recommends \
    imagemagick \
    ghostscript \
 && rm -rf /var/lib/apt/lists/*

RUN set -xe \
  && wget "https://sourceforge.net/projects/logicaldoc/files/distribution/LogicalDOC%20CE%207.7/logicaldoc-7.7.6-tomcat-bundle.zip/download" -O /usr/local/logicaldoc-tomcat-bundle.zip

RUN set -xe \
  && unzip /usr/local/logicaldoc-tomcat-bundle.zip -d /usr/local/ \
  && mv /usr/local/logicaldoc-7.7.6-tomcat-bundle /usr/local/logicaldoc \    
  && rm /usr/local/logicaldoc-tomcat-bundle.zip

#fix for Java 9 - Java 10 (also defines max memory available to the JAVA VM)
COPY setenv.sh /usr/local/logicaldoc/tomcat/bin

RUN set -xe \
  && unzip /usr/local/logicaldoc/tomcat/webapps/logicaldoc.war -d /usr/local/logicaldoc/tomcat/webapps/logicaldoc/ \
  && rm /usr/local/logicaldoc/tomcat/webapps/logicaldoc.war

ENV PATH $PATH:$CATALINA_HOME/bin

COPY ./conf/* /usr/local/logicaldoc/tomcat/webapps/logicaldoc/WEB-INF/classes/

RUN set -xe \
  && ln -s /usr/local/logicaldoc /opt/logicaldoc

# that is to get the HSQLDB (internal database) already initialized and ready to use
ADD repository.tar /opt/logicaldoc/

RUN apt-get update \
    && apt-get install -y vim nano \
    && apt-get -y clean

#volumes for persistent storage
VOLUME /opt/logicaldoc/repository

#port to connect to
EXPOSE 8080

RUN chmod +x /opt/logicaldoc/tomcat/bin/catalina.sh

CMD /opt/logicaldoc/tomcat/bin/catalina.sh run
