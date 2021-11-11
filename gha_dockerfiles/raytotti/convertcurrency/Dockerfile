FROM openjdk:11.0.12-jre-slim
ARG JAR_FILE=target/*.jar
COPY ${JAR_FILE} app.jar
ENTRYPOINT ["java", "-Xmx512m", "-Dserver.port=${PORT}", "-jar", "/app.jar"]