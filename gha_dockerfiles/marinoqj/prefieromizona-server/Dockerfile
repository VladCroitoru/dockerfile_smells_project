FROM openjdk:11-jdk
VOLUME /tmp
ARG JAR_FILE=/target/prefieromizona.jar
COPY ${JAR_FILE} app.jar
ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar", "-Dspring.profiles.active=prod", "/app.jar"]