FROM openjdk:16-jdk-slim

COPY build/libs/kotik-bot-0.0.1-SNAPSHOT.jar /service.jar

USER 999
ENTRYPOINT ["java", "-jar", "/service.jar"]
