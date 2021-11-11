#FROM openjdk:8-jdk-alpine
#ARG JAR_FILE=target/*.jar
#COPY ${JAR_FILE} app.jar
#ENTRYPOINT ["java","-jar","/app.jar"]
#

FROM maven:3.8.2-openjdk-11-slim as build
COPY src /home/app/src
COPY pom.xml /home/app
RUN mvn -f /home/app/pom.xml clean package -DskipTests=True

FROM openjdk:11.0-jdk-slim-buster
COPY --from=build /home/app/target/santas-grotto-0.0.1-SNAPSHOT.jar /usr/local/lib/demo.jar
ENV SPRING_PROFILES_ACTIVE=prod
EXPOSE 8080
ENTRYPOINT ["java","-jar","/usr/local/lib/demo.jar"]