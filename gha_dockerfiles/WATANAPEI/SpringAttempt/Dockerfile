# build application
FROM maven:3.6.1-amazoncorretto-11 as build
RUN mkdir -p /opt/springattempt/src
# pom.xml だけデプロイし、先に依存解決
COPY pom.xml /opt/springattempt
WORKDIR /opt/springattempt
# RUN mvn -B package; echo ""
RUN mvn -B dependency:resolve dependency:resolve-plugins

COPY src /opt/springattempt/src
RUN mvn -B package

# build docker image
FROM openjdk:11
RUN apt-get update -y && \
  mkdir -p /opt/app/
COPY --from=build /opt/springattempt/target/springattempt-0.0.1-SNAPSHOT.jar /opt/app/
EXPOSE 8080
CMD ["java", "-jar", "/opt/app/springattempt-0.0.1-SNAPSHOT.jar"]


