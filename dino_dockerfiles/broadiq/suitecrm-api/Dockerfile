FROM anapsix/alpine-java:8_jdk
#FROM openjdk:latest

MAINTAINER John S. Lutz <jlutz@broadiq.com>

ENV SERVER_PORT 80

VOLUME /tmp
ADD suitecrm.api-0.1.0.jar app.jar


EXPOSE $SERVER_PORT

#ENTRYPOINT exec java -Xmx256m -Djava.security.egd=file:/dev/./urandom -jar /app.jar
ENTRYPOINT ["java","-Xmx256m", "-Djava.security.egd=file:/dev/./urandom","-jar","/app.jar"]
