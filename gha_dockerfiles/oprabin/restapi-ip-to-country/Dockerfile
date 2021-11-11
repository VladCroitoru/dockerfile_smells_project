FROM maven:3.6.0-jdk-11-slim AS build-tool

COPY restapi-axon-ivy/ /home/app/restapi-axon-ivy
RUN mvn -f /home/app/restapi-axon-ivy/pom.xml clean package -X


FROM axonivy/axonivy-engine:8.0 AS official-axon-engine
COPY --chown=ivy:ivy --from=build-tool /home/app/restapi-axon-ivy/target/restapi-axon-ivy-1.0.0.iar deploy/restapi-axon-ivy/
