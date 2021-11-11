FROM openjdk:8
ADD target/slack-integration.jar slack-integration.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "slack-integration.jar"]