FROM gradle:6.8.3-jdk11 AS build
COPY --chown=gradle:gradle . /home/gradle/src
WORKDIR /home/gradle/src
RUN gradle build --no-daemon -x test

FROM openjdk:11
EXPOSE 8070
COPY --from=build /home/gradle/src/center/build/libs/*.jar center.jar

ENTRYPOINT ["java", "-Dspring.profiles.active=dev", "-jar", "/center.jar"]
