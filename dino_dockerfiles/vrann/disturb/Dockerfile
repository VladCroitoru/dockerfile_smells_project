# VERSION 1.0

# the base image is a trusted ubuntu build with java 7 (https://index.docker.io/u/dockerfile/java/)
FROM dockerfile/java:oracle-java7

# that's me!
MAINTAINER Eugene Tulika vranen@gmail.com

RUN sudo apt-get update && apt-get install -y \
    maven

WORKDIR /app
ADD src /app/src
ADD pom.xml /app/pom.xml
RUN mvn package

# run the (java) server as the daemon user
USER daemon
EXPOSE 1366

# run the server when a container based on this image is being run
ENTRYPOINT ["java", "-jar", "/app/target/disturb-1.0.0.jar"]