FROM adoptopenjdk/openjdk11:alpine
ARG JAR_FILE=build/libs/\*.jar
ARG PROFILE=local-docker
ENV PROFILE_ENV ${PROFILE}
COPY ${JAR_FILE} app.jar
ENTRYPOINT ["java", "-jar", "/app.jar", "--spring.profiles.active=${PROFILE_ENV}"]