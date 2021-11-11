FROM tomcat:9.0.48-jdk16-openjdk
MAINTAINER https://github.com/sierbb

COPY target/numeral-converter.war /usr/local/tomcat/webapps/ROOT.war
EXPOSE 8080
CMD ["catalina.sh", "run"]
