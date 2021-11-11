FROM openjdk:11-jre-slim
LABEL maintainer = "BTS"
VOLUME /tmp
ARG JAR_FILE=./*.jar
ADD ${JAR_FILE} app.jar
EXPOSE 8761
ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","/app.jar"]
