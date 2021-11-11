FROM openjdk:8-jdk-alpine
ARG JAR_FILE=target/dnd5.jar
WORKDIR /opt/app
COPY ${JAR_FILE} dnd5.jar
ENTRYPOINT ["java","-jar","dnd5.jar"]
