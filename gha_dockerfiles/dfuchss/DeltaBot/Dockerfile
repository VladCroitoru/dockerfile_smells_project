FROM maven:3-eclipse-temurin-17 as builder

WORKDIR /usr/src/bot
COPY src src
COPY pom.xml pom.xml
RUN mvn clean package

FROM eclipse-temurin:17-alpine

ENV RUN_IN_DOCKER true
ENV DISCORD_TOKEN MY_TOKEN
ENV TZ=Europe/Berlin
ENV DB_PATH /usr/src/bot/data/data.sqlite

WORKDIR /usr/src/bot
COPY --from=builder /usr/src/bot/target/deltabot-*-jar-with-dependencies.jar deltabot.jar

VOLUME /usr/src/bot/data

ENTRYPOINT java -jar /usr/src/bot/deltabot.jar
