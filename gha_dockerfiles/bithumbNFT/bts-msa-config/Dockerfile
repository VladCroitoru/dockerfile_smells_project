FROM openjdk:11-jre-slim
LABEL maintainer = "BTS"
VOLUME /tmp
ARG JAR_FILE=config-server-0.0.1-SNAPSHOT.jar
ADD ${JAR_FILE} app.jar
EXPOSE 8888
ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","/app.jar"]