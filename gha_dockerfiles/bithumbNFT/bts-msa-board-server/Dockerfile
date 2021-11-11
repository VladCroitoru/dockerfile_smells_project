FROM openjdk:11-jre-slim
LABEL maintainer="bts"
VOLUME /tmp
ARG JAR_FILE=./*.jar
ADD ${JAR_FILE} app.jar
EXPOSE 8080
ENTRYPOINT ["java","-Dspring.data.mongodb.uri=mongodb://mongo:27017/bts-board-db","-Djava.security.egd=file:/dev/./urandom","-jar","/app.jar"]