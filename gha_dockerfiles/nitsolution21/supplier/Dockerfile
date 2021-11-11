FROM openjdk:8-jdk-alpine
VOLUME /tmp
ADD target/supplier-0.0.1-SNAPSHOT.war prod.jar
ENTRYPOINT ["java","-jar","/prod.jar"]