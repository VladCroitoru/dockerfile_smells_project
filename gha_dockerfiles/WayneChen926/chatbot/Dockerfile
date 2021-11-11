FROM gradle:7.2.0-jdk11-hotspot AS build
COPY --chown=gradle:gradle . /home/gradle/src
WORKDIR /home/gradle/src
RUN gradle build 

FROM adoptopenjdk/openjdk11:jdk-11.0.8_10-alpine

ENV TZ=Asia/Taipei
ENV JAVA_OPTS="-server -XX:+UseG1GC -verbose:gc -Xlog:gc:stdout -XX:InitialRAMPercentage=50 -XX:MaxRAMPercentage=90 -XX:MinRAMPercentage=50 -XX:-UseContainerSupport"

EXPOSE 8080

RUN mkdir /app

COPY --from=build /home/gradle/src/build/libs/*-0.0.1-SNAPSHOT.jar /app/app.jar

ENTRYPOINT ["java","-jar","/app/app.jar"]