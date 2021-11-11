FROM techio/maven3-builder:1.4

ENV TECHIO_RUN_DIR /project/answer

# Copy files
COPY docker/junit-runner /usr/src/codingame/junit-runner/
COPY target/java-maven3-junit4-runner-0.0.1-SNAPSHOT-jar-with-dependencies.jar /usr/src/codingame/junit-runner/junit-runner.jar

ENTRYPOINT ["/usr/src/codingame/junit-runner/junit-runner"]
