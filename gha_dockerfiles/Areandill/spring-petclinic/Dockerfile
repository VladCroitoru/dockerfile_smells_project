FROM openjdk:8-jre-alpine
WORKDIR /app
COPY ./target/*.jar .
ENTRYPOINT ["java", "-jar", "spring-petclinic-2.5.0-SNAPSHOT.jar"]
EXPOSE 8080:8080
