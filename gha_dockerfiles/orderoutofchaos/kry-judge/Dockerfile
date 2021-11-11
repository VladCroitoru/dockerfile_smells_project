FROM openjdk:16-jdk-alpine
ARG JAR_FILE=./build/libs/*.jar
COPY ${JAR_FILE} app.jar
COPY wait-for .
RUN ["chmod", "+x", "./wait-for"]
EXPOSE 8080
CMD ["java", "-jar", "/app.jar"]
