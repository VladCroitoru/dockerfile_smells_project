FROM openjdk:11.0.10-slim
WORKDIR /appnator
COPY target/*.jar api.jar
EXPOSE 8443 8080
ENTRYPOINT ["java", "-Djava.security.egd=file:/dev/./urandom", "-jar", "/appnator/api.jar"]

