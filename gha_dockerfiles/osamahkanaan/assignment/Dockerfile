FROM openjdk:8-jdk-alpine
VOLUME /temp
ADD target/assignment.jar app.jar
ENTRYPOINT ["java", "-jar", "/app.jar"]

#CMD ["/bin/sh"]
