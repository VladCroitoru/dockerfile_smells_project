FROM openjdk:11.0.12-slim
EXPOSE 8080
ARG JAR_FILE=build/libs/backend-0.0.1-SNAPSHOT.jar
ADD ${JAR_FILE} app.jar
ENTRYPOINT ["java","-Dspring.profiles.active=dev", "-jar","/app.jar"]