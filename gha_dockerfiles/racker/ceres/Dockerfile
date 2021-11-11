# docker build -t ceres-in-docker:0.5 .
# this file is for local development use only

FROM adoptopenjdk/openjdk14:alpine-jre

COPY target/ceres-0.0.1-SNAPSHOT.jar ceres-in-docker.jar

EXPOSE 8080
ENTRYPOINT ["java", "-jar", "ceres-in-docker.jar"]
