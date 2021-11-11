FROM openjdk:17-ea-11-jdk-slim
VOLUME /tmp
COPY /target/user-1.0.jar User.jar
ENTRYPOINT ["java", "-jar", "User.jar"]