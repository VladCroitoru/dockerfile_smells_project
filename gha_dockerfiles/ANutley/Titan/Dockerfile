FROM gradle:7.2.0-jdk8 AS app
WORKDIR /build
COPY . ./
RUN ./gradlew build

FROM openjdk:8
WORKDIR /bot
VOLUME /bot
COPY --from=app /build/build/libs/Titan-1.0-SNAPSHOT-all.jar /bot
CMD ["java", "-jar", "Titan-1.0-SNAPSHOT-all.jar"]