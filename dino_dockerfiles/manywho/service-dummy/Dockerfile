FROM maven:slim AS build
WORKDIR /usr/src/app
COPY src src
COPY pom.xml pom.xml
RUN mvn clean package

FROM openjdk:8-jre-slim
EXPOSE 8080
EXPOSE 8081

COPY src/main/resources/server_keystore.jks /usr/src/app/target/server_keystore.jks
COPY src/main/resources/server_truststore.jks /usr/src/app/target/server_truststore.jks

COPY --from=build /usr/src/app/target/service-dummy.jar /usr/src/app/target/service-dummy.jar

ENTRYPOINT ["java", "-jar", "/usr/src/app/target/service-dummy.jar"]
