FROM openjdk:11-jre-slim
VOLUME /tmp
ARG JAR_FILE=./build/libs/consumer-0.0.1-SNAPSHOT.jar
ADD ${JAR_FILE} app.jar
EXPOSE 5020
ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","/app.jar"]