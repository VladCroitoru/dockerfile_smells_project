ARG OPENJDK_TAG=8u292
ARG SBT_VERSION=1.5.4
FROM mozilla/sbt:${OPENJDK_TAG}_${SBT_VERSION} AS build

WORKDIR /project
COPY . .
RUN ["sbt", "assembly"]

FROM openjdk:14-jdk-alpine
COPY --from=build project/target/scala-3.0.0/ergoindex-backend-0.0.1.jar app.jar
ENTRYPOINT ["java","-jar","/app.jar"]
