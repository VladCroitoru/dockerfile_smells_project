FROM tomcat:8.0-alpine

LABEL maintainer="fuadmonsoon"

ADD *.war /usr/local/tomcat/webapps/webcustomertracker.war

EXPOSE 8080

CMD ["catalina.sh", "run"]
