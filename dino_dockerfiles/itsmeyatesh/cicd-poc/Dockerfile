FROM maven:3.5-jdk-8-alpine as build
WORKDIR /app
COPY .  /app
RUN mvn install

FROM maven:3.5-jdk-8-alpine
WORKDIR /app
COPY --from=build /app/target/GreetingService-0.0.1-SNAPSHOT.jar app/GreetingService-0.0.1-SNAPSHOT.jar
EXPOSE 8080
ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","app/GreetingService-0.0.1-SNAPSHOT.jar"]
