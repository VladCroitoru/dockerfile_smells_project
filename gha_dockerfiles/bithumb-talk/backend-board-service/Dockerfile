FROM openjdk:17-ea-11-jdk-slim
WORKDIR /server
ARG JAR_FILE=./build/libs/board-0.0.1-SNAPSHOT.jar
ADD ${JAR_FILE} board-service.jar
#COPY ./elastic-apm-agent-*.jar /elastic-apm-agent.jar
EXPOSE 7000
ENTRYPOINT ["java", "-jar", "board-service.jar"]

