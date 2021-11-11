FROM sdempsay/docker-felix-basic
MAINTAINER Shawn Dempsay <shawn@dempsay.org>

#
# Web console, file deploy, logging, scr
#
ADD http://mirrors.ibiblio.org/apache/felix/org.apache.felix.webconsole-4.2.2-all.jar /opt/felix/current/bundle/
ADD http://repo1.maven.org/maven2/org/apache/felix/org.apache.felix.http.api/2.3.0/org.apache.felix.http.api-2.3.0.jar /opt/felix/current/bundle/
ADD http://repo1.maven.org/maven2/org/apache/felix/org.apache.felix.eventadmin/1.3.2/org.apache.felix.eventadmin-1.3.2.jar /opt/felix/current/bundle/
ADD http://repo1.maven.org/maven2/org/apache/felix/org.apache.felix.configadmin/1.8.0/org.apache.felix.configadmin-1.8.0.jar /opt/felix/current/bundle/
ADD http://repo1.maven.org/maven2/org/apache/felix/org.apache.felix.http.jetty/2.3.0/org.apache.felix.http.jetty-2.3.0.jar /opt/felix/current/bundle/
ADD http://repo1.maven.org/maven2/org/apache/felix/org.apache.felix.http.servlet-api/1.0.0/org.apache.felix.http.servlet-api-1.0.0.jar /opt/felix/current/bundle/
ADD http://repo1.maven.org/maven2/org/apache/felix/org.apache.felix.webconsole.plugins.event/1.1.0/org.apache.felix.webconsole.plugins.event-1.1.0.jar /opt/felix/current/bundle/
ADD http://repo1.maven.org/maven2/org/apache/felix/org.apache.felix.webconsole.plugins.ds/1.0.0/org.apache.felix.webconsole.plugins.ds-1.0.0.jar /opt/felix/current/bundle/
ADD http://repo1.maven.org/maven2/org/apache/felix/org.apache.felix.metatype/1.0.10/org.apache.felix.metatype-1.0.10.jar /opt/felix/current/bundle/
ADD http://repo1.maven.org/maven2/org/apache/felix/org.apache.felix.scr/1.8.2/org.apache.felix.scr-1.8.2.jar /opt/felix/current/bundle/
ADD http://repo1.maven.org/maven2/org/apache/felix/org.apache.felix.fileinstall/3.4.0/org.apache.felix.fileinstall-3.4.0.jar /opt/felix/current/bundle/
ADD http://repo1.maven.org/maven2/org/apache/felix/org.apache.felix.log/1.0.1/org.apache.felix.log-1.0.1.jar /opt/felix/current/bundle/
EXPOSE 8080
EXPOSE 8000
VOLUME /opt/felix/current/load
CMD cd /opt/felix/current && java -Xdebug -Xnoagent -Xrunjdwp:transport=dt_socket,address=8000,server=y,suspend=n -jar bin/felix.jar
