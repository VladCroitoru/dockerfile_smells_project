# syntax=docker/dockerfile:1

# build stage
FROM gradle:jdk8-hotspot AS build
WORKDIR /package
# copy gradle build script files
COPY build.gradle.kts gradle.properties settings.gradle.kts ./
# copy source folder
COPY src ./src
# build fat jar
RUN gradle shadowJar
# run stage
FROM openjdk:8u302-jre AS run
WORKDIR /app
# copy jar
COPY --from=build /package/build/libs/ ./
# run jar
CMD ["java", "-jar", "./baodatui.jar"]