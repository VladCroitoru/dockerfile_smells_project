FROM openjdk:8-jdk-alpine
VOLUME /tmp
COPY target/pm-mock-*.jar app.jar
ENTRYPOINT ["java", "-jar", "app.jar"]