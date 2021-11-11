FROM tomcat:9.0.24-jdk11-adoptopenjdk-hotspot
RUN rm -rf /usr/local/tomcat/conf/logging.properties /usr/local/tomcat/webapps/*
COPY target/xmlconv.war /usr/local/tomcat/webapps/ROOT.war
COPY docker/server.xml  /usr/local/tomcat/conf/server.xml