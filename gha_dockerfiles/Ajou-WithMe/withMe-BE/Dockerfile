FROM openjdk:11
ARG JAR_FILE=build/libs/main-0.0.1-SNAPSHOT.jar
COPY ${JAR_FILE} /app.jar
ENTRYPOINT ["sh","-c","java -Dspring.profiles.active=prod ${JAVA_OPTS} -jar /app.jar"]

