# Base the container image off of JDK 8
FROM openjdk:8

# The port that YOU should expose when you run this in a container
# see https://docs.docker.com/engine/reference/builder/#expose
EXPOSE 8081

# Add the server.jar and set entry point
COPY service/target/service-1.0-SNAPSHOT-jar-with-dependencies.jar server.jar
ENTRYPOINT java -jar server.jar
