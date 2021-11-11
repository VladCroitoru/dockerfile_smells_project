FROM eclipse-temurin:17-jdk-alpine
ARG PROFILE
ENV PROFILE_VAR=$PROFILE
VOLUME /tmp
ADD build/libs/squash-rest-app-1.0.0-SNAPSHOT.jar app.jar
ENTRYPOINT ["/bin/bash", "-c", "java","-Dspring.profiles.active=$PROFILE_VAR","-jar","/app.jar"]
EXPOSE 80