FROM maven:slim AS build
WORKDIR /usr/src/app
COPY src src
COPY pom.xml pom.xml
RUN mvn clean package

FROM openjdk:8-jre-slim
EXPOSE 8080
COPY --from=build /usr/src/app/target/service-identity.jar /usr/src/app/target/service.jar
ENTRYPOINT ["java", "-jar", "/usr/src/app/target/service.jar"]
