FROM maven:3.6-jdk-14 as BUILD

RUN mkdir -p /usr/src/app

COPY src /usr/src/app/src
COPY pom.xml /usr/src/app
RUN mvn -f /usr/src/app/pom.xml clean package

FROM openjdk:14-alpine
 
COPY --from=BUILD /usr/src/app/target/MusicMeterParser.jar /usr/src/app/MusicMeterParser.jar

EXPOSE 8080
EXPOSE 8081

ENTRYPOINT java -jar /usr/src/app/MusicMeterParser.jar server
