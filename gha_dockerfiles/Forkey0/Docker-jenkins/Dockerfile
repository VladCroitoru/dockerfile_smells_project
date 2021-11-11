FROM openjdk:11-jre-slim as builder
EXPOSE  3000
ADD target/inetum-docker.jar inetum-docker.jar
ENTRYPOINT ["java","-jar","/inetum-docker.jar"]