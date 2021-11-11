FROM tomcat:8.5.28-jre8
ADD browser-0.0.1.war /usr/local/tomcat/webapps/
#ADD server.xml /usr/local/tomcat/conf/
EXPOSE 8080
CMD chmod +x /usr/local/tomcat/bin/catalina.sh
CMD ["catalina.sh", "run"]
