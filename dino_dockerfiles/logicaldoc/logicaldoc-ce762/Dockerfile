FROM ubuntu:16.04

MAINTAINER Alessandro Gasparini <developers@logicaldoc.com>

ENV CATALINA_HOME /usr/local/tomcat
ENV TOMCAT_VERSION 8.0.36
ENV JAVA_HOME /usr/local/java
ENV ORACLE_JAVA_HOME /usr/lib/jvm/java-8-oracle/
ENV TERM xterm

RUN set -xe \
  && apt-get update \
  && apt-get install -y python-software-properties software-properties-common \
  && echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-selections \
  && echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-selections \
  && add-apt-repository -y ppa:webupd8team/java \
  && apt-get update \
  && apt-get install -y oracle-java8-installer imagemagick ghostscript wget curl unzip sudo tar

RUN set -xe \
  && ln -s $ORACLE_JAVA_HOME $JAVA_HOME

RUN set -xe \
  && wget "https://sourceforge.net/projects/logicaldoc/files/distribution/LogicalDOC%20CE%207.6/logicaldoc-7.6.2-tomcat-bundle.zip/download" -O /usr/local/logicaldoc-tomcat-bundle.zip

RUN set -xe \
  && unzip /usr/local/logicaldoc-tomcat-bundle.zip -d /usr/local/ \
  && rm /usr/local/logicaldoc-tomcat-bundle.zip \
  && ln -s $CATALINA_HOME /opt/logicaldoc

RUN set -xe \
  && unzip /usr/local/tomcat/webapps/logicaldoc.war -d /usr/local/tomcat/webapps/logicaldoc/ \
  && rm /usr/local/tomcat/webapps/logicaldoc.war

ENV PATH $PATH:$CATALINA_HOME/bin

COPY ./conf/* /usr/local/tomcat/webapps/logicaldoc/WEB-INF/classes/

# that is to get the HSQLDB (internal database) already initialized and ready to use
ADD repository.tar /opt/logicaldoc/

# remove unwanted web-applications that comes with standard tomcat 8.0.x standard distribution
RUN set -xe \
  && rm -rf /usr/local/tomcat/webapps/docs \
  && rm -rf /usr/local/tomcat/webapps/examples \
  && rm -rf /usr/local/tomcat/webapps/host-manager \
  && rm -rf /usr/local/tomcat/webapps/manager \
  && rm -f /usr/local/tomcat/webapps/ROOT/index.jsp

COPY index.jsp /usr/local/tomcat/webapps/ROOT

RUN set -xe \
  && apt-get -y clean

#volumes for persistent storage
VOLUME /opt/logicaldoc/repository

#port to connect to
EXPOSE 8080

RUN chmod +x /opt/logicaldoc/bin/catalina.sh

CMD /opt/logicaldoc/bin/catalina.sh run
