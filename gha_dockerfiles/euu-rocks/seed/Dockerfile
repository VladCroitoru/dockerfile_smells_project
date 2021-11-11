FROM openjdk:11-jdk-buster
VOLUME /tmp
EXPOSE 8080
ARG JAR_FILE=./target/seed-*.jar
COPY ${JAR_FILE} app.jar
ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","/app.jar"]