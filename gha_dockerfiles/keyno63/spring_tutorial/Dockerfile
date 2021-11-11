FROM openjdk:18-jdk-alpine

ARG JAR_FILE=build/libs/spring_tutorial-0.0.1-SNAPSHOT.jar
COPY ${JAR_FILE} app.jar

ENTRYPOINT ["java","-jar","/app.jar"]
