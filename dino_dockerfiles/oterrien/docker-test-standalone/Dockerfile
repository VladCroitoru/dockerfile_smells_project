FROM openjdk:8u111-jdk

COPY target/docker-test-standalone.jar docker.jar

EXPOSE 8080

CMD ["java", "-jar", "docker.jar"]