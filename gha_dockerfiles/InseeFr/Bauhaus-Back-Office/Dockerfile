FROM maven:3.6.2 as mvn
WORKDIR /bauhaus
COPY ./ /bauhaus/
RUN mvn -B -f /bauhaus/pom.xml package


FROM tomcat:8-jdk8
COPY --from=mvn bauhaus/target/bauhaus.war /usr/local/tomcat/webapps/
ADD ./config/start.sh /usr/local/tomcat
RUN chmod +x /usr/local/tomcat/start.sh
ENTRYPOINT [ "/usr/local/tomcat/start.sh"]
CMD ["catalina.sh", "run"]
