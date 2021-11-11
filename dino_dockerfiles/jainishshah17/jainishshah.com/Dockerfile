FROM damm/java8

MAINTAINER Jainishshah@yahoo.com

EXPOSE 8080

ENV TOMCAT_VERSION 8.0.21

RUN wget --quiet --no-cookies http://archive.apache.org/dist/tomcat/tomcat-8/v${TOMCAT_VERSION}/bin/apache-tomcat-${TOMCAT_VERSION}.tar.gz -O /tmp/catalina.tar.gz

RUN tar xzf /tmp/catalina.tar.gz -C /opt

RUN mv /opt/apache-tomcat-${TOMCAT_VERSION} /opt/tomcat

RUN rm /tmp/catalina.tar.gz

# Remove unneeded apps

RUN rm -rf /opt/tomcat/webapps/*

RUN apt-get update

ADD ROOT.war /opt/tomcat/webapps/

ENV CATALINA_HOME /opt/tomcat

ENV PATH $PATH:$CATALINA_HOME/bin

# Start Tomcat

CMD /opt/tomcat/bin/catalina.sh start && tail -f /opt/tomcat/logs/catalina.out
