FROM maven:3.6.0-jdk-7-alpine as built
WORKDIR /tmp/
COPY src ./src
COPY pom.xml .
RUN mvn clean package
FROM tomcat:9.0-alpine
COPY --from=built /tmp/target/hello-1.0.war /usr/local/tomcat/webapps/hello-1.0.war
EXPOSE 8080





