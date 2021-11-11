FROM tomcat:8.0.20-jre8
COPY tomcat-users.xml /usr/local/tomcat/conf/
COPY target/grants.war /usr/local/tomcat/webapps/
RUN sh /usr/local/tomcat/bin/catalina.sh stop
RUN sleep 30
RUN sh /usr/local/tomcat/bin/catalina.sh start



