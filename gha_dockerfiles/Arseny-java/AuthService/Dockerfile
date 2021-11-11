FROM openjdk:8-jdk-alpine
EXPOSE 8080
ADD target/AuthService-0.0.1-SNAPSHOT.jar /authorize.jar
ENTRYPOINT ["java", "-jar", "/authorize.jar"]