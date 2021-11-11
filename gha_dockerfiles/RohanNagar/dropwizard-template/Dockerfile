FROM openjdk:11-jre

LABEL maintainer "Rohan Nagar <rohannagar11@gmail.com>"

COPY ./application/target/application-*.jar app.jar

EXPOSE 8080 8081 8443 8444
ENTRYPOINT ["java", "-jar", "/app.jar", "server", "/home/config/config.yaml"]
