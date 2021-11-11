FROM maven:3.5.2-jdk-8 as mavenBuild
COPY pom.xml .
COPY src ./src/
RUN ["mvn"]

FROM java:8
COPY --from=mavenBuild ./target/slow-kafka-consumer-1.0.0-SNAPSHOT-jar-with-dependencies.jar .
ENV BOOTSTRAP_SERVERS kafka:9092
ENV TOPIC input-topic
ENV GROUP slow-consumer
CMD [ "bash", "-c", "java -jar slow-kafka-consumer-1.0.0-SNAPSHOT-jar-with-dependencies.jar --bootstrap-servers ${BOOTSTRAP_SERVERS} --topics ${TOPIC} --group ${GROUP}"]