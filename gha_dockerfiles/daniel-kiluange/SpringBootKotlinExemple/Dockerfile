FROM openjdk:11-slim as builder
WORKDIR /usr/src
COPY . .

RUN ./gradlew clean build --info

FROM openjdk:11-slim
WORKDIR /usr/src/app

COPY --from=builder /usr/src/build/libs/*SNAPSHOT.jar app.jar

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

EXPOSE 8080

ENTRYPOINT exec java -jar app.jar