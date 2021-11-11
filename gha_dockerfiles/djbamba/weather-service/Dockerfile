FROM openjdk:8-jdk-alpine
COPY target/*.jar weather-service.jar
ENTRYPOINT ["java","-Dspring.profiles.active=docker", "-jar", "/weather-service.jar"]
EXPOSE 8182
