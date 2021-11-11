FROM maven:3-openjdk-17 AS builder

COPY src /home/app/src
COPY pom.xml /home/app
RUN mvn -f /home/app/pom.xml clean test package appassembler:assemble

##############

FROM openjdk:17-alpine

COPY --from=builder /home/app/target/appassembler/ app

ENTRYPOINT ["app/bin/shoutbotx"]
