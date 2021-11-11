FROM tomcat:8.0

LABEL maintainer="Israq TCS"

ADD ./target/jenkins-git-integration.war /usr/local/tomcat/webapps/

EXPOSE 8080

CMD ["catalina.sh", "run"]
