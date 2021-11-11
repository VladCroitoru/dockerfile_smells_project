FROM maven:3-openjdk-16-slim AS build
WORKDIR /app
COPY . .
RUN mvn -B package

FROM tomcat:10-jdk16-openjdk-slim
COPY --from=build /app/target/web-app-1.0.war $CATALINA_HOME/webapps/ROOT.war
COPY apache-tomcat-10.0.11/conf/server.xml $CATALINA_HOME/conf
COPY apache-tomcat-10.0.11/conf/certs $CATALINA_HOME/conf/certs
EXPOSE 8080
EXPOSE 8443
