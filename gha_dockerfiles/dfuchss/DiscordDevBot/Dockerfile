FROM maven:3-jdk-11 as builder

WORKDIR /usr/src/bot
COPY src src
COPY pom.xml pom.xml
RUN mvn clean package

FROM azul/zulu-openjdk-alpine:11

ENV DISCORD_TOKEN MY_TOKEN
ENV CONF_PATH /usr/src/bot/config/config.json

WORKDIR /usr/src/bot
COPY --from=builder /usr/src/bot/target/devbot-*-jar-with-dependencies.jar devbot.jar

VOLUME /usr/src/bot/config
ENTRYPOINT java -jar /usr/src/bot/devbot.jar
