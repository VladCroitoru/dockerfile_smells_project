FROM eclipse-temurin:11-jdk
COPY target/*.jar /usr/src/app/app.jar
WORKDIR /usr/src/app
ENV SERVER_PORT 8080
EXPOSE 8080
USER 1001
ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","app.jar"]
