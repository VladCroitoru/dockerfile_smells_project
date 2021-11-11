FROM openjdk:8-jdk-alpine
COPY target/*.jar go-fish-service.jar
ENTRYPOINT ["java","-Dspring.profiles.active=docker", "-jar", "/go-fish-service.jar"]
EXPOSE 8181
