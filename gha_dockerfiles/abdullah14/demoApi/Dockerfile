#FROM maven:3.6.0-jdk-8
#EXPOSE 8080
#ADD /target/demo.api-0.0.1-SNAPSHOT.jar demo.api.jar
#ENTRYPOINT ["java", "-jar", "demo.api.jar"]

FROM maven:3.6.0-jdk-8
ARG JAR_FILE=target/*.jar
COPY ${JAR_FILE} app.jar
ENTRYPOINT ["java","-jar","/app.jar"]
