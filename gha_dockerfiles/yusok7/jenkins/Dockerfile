FROM openjdk:11-jre-slim
ARG JAR_FILE=./build/libs/jenkins-0.0.1-SNAPSHOT.jar
ADD ${JAR_FILE} app.jar
ENTRYPOINT ["java","-jar","/app.jar"]