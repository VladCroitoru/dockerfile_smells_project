FROM openjdk:8-jre-alpine
EXPOSE 8080
COPY build/libs/simpleRegions-0.0.1-SNAPSHOT-plain.jar app.jar
ENTRYPOINT [ "java", "-jar", "/app.jar"]