FROM openjdk:16-jdk-alpine
ARG JAR_FILE=target/*jar
COPY ${JAR_FILE} app.jar
CMD ["java","-Djava.security.egd=file:/dev/./urandom","-jar","/app.jar"]
