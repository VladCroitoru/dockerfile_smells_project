FROM tomcat:jdk11-corretto

LABEL name="mw-image"

ADD sample.war /usr/local/tomcat/webapps/
ADD index.html /usr/local/tomcat/webapps/sample/

EXPOSE 8080

CMD ["catalina.sh", "run"]
