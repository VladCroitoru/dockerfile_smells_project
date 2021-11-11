FROM openjdk:8-jdk-alpine
VOLUME /tmp
COPY target/desafio-*.jar app.jar
ENTRYPOINT ["java", "-jar", "/app.jar"]