FROM openjdk:17-ea-11-jdk-slim

WORKDIR /server

COPY ./build/libs/demo-0.0.1-SNAPSHOT.jar jenkins-test.jar

ENTRYPOINT ["java", "-jar", "jenkins-test.jar"]