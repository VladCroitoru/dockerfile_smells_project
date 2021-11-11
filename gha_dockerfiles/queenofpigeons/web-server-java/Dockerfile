FROM openjdk:15-jdk-alpine

ARG JAR_FILE
COPY ${JAR_FILE} app.jar

ENV HOST 127.0.0.1  # default value
ENV PORT 8080  # default value

ENTRYPOINT ["java","-jar", "-Dserver.addres=${HOST}","-Dserver.port=${PORT}", "/app.jar"]
