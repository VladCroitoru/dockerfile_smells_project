FROM openjdk:8-jdk-alpine
COPY target/container-ci-demo.jar container-ci-demo.jar
EXPOSE 8080
ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom", "-jar", "container-ci-demo.jar"]
