FROM tomcat:7-jre8-alpine

MAINTAINER David CROSSON <crosson.david@gmail.com>


ENV PURL http://www.janalyse.fr/primesui/primesui.war
ADD $PURL $CATALINA_HOME/webapps/

###ENV JURL http://labs.consol.de/maven/repository/org/jolokia/jolokia-war/1.2.3/jolokia-war-1.2.3.war
###ADD $JURL $CATALINA_HOME/webapps/

ADD setenv.sh  $CATALINA_HOME/bin/
ADD server.xml $CATALINA_HOME/conf/

ENV PRIMESUI_CACHE   true
ENV PRIMESUI_TESTING false
ENV PRIMESUI_SESSION true

