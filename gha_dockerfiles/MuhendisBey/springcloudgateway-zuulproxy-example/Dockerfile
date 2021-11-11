#FROM azul/zulu-openjdk-alpine:11-jre # this make a problem for creating eureka client
FROM openjdk:11-jre-slim
ARG JAR_FILE_NAME
WORKDIR /opt/app
COPY ./target/$JAR_FILE_NAME ./app.jar
ENTRYPOINT ["java", "-jar", "app.jar"]