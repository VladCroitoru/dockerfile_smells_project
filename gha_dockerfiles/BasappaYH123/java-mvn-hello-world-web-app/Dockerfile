FROM maven:3.8.2-openjdk-8-slim as build
WORKDIR /dir
COPY . .
RUN mvn package
FROM tomcat:jre8-temurin-focal
COPY --from=build /dir/target/mvn-hello-world.war /usr/local/tomcat/webapps
