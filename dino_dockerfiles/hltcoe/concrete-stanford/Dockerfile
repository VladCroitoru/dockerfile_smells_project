FROM maven:3-jdk-8 as builder

ENV MAVEN_OPTS "-Dmaven.repo.local=/cache/.m2/repository"
ENV MAVEN_CLI_OPTS "--batch-mode --errors --fail-at-end --show-version"

RUN mkdir build
WORKDIR build

COPY . .

RUN mvn $MAVEN_CLI_OPTS clean install -DskipTests

FROM openjdk:8-jre-alpine

COPY --from=builder build/annotate/target/concrete*uberjar.jar /app.jar

ENTRYPOINT ["/usr/bin/java", "-jar", "/app.jar"]
CMD ["--help"]
