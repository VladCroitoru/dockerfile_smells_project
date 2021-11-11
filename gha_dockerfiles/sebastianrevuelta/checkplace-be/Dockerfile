FROM openjdk:17-jdk-alpine
ARG JAR_FILE=./target/checkplace-0.0.1-SNAPSHOT.jar
COPY ${JAR_FILE} /opt/checkplace-be.jar
EXPOSE 8080
CMD ["java", "-jar", "/opt/checkplace-be.jar"]
