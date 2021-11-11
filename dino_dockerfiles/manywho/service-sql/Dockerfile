FROM maven:slim AS build
WORKDIR /usr/src/app
COPY src src
COPY pom.xml pom.xml
# TODO: Fix whatever stops the tests from completely breaking in Bamboo
RUN mvn clean package -DskipTests=true

FROM openjdk:8-jre-slim
EXPOSE 8080
COPY --from=build /usr/src/app/target/sql-2.0-SNAPSHOT.jar /usr/src/app/target/service.jar
ENTRYPOINT ["java", "-jar", "/usr/src/app/target/service.jar"]
