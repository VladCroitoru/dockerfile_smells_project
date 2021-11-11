#FROM adoptopenjdk/openjdk15:alpine
#
#ARG JAR_FILE=target/*.jar
#COPY ${JAR_FILE} app.jar
#ENTRYPOINT ["java","-jar","/app.jar"]

#FROM adoptopenjdk/openjdk15:alpine
#VOLUME /tmp
#ADD target/notes-0.0.1-SNAPSHOT.jar app.jar
#ENTRYPOINT ["java","-jar","/app.jar"]

FROM openjdk:16-alpine
ARG JAR_FILE=notes/notes/target/notes-0.0.1-SNAPSHOT.jar
COPY ${JAR_FILE} app.jar
ENTRYPOINT ["java","-jar","/app.jar"]