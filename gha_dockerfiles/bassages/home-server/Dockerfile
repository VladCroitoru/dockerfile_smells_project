FROM openjdk:10-jdk

MAINTAINER nl.homeserver

RUN mkdir -p /opt/home-server
COPY build/libs/home-server*.jar /opt/home-server
COPY application-docker.properties /opt/home-server

WORKDIR /opt/home-server

EXPOSE 8080

VOLUME /var/home-server/database

ENTRYPOINT ["java", "-jar", "-Dspring.profiles.active=docker", "/opt/home-server/home-server-backend-1.0.0.jar"]
