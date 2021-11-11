FROM openjdk:11
ADD target/car-service.jar car-service.jar
ENTRYPOINT ["java", "-jar","-Dspring.profiles.active=docker", "car-service.jar"]
EXPOSE 8080