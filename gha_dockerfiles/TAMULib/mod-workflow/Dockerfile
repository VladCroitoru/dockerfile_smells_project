# build base image
FROM maven:3-openjdk-11-slim as maven

# copy pom.xml
COPY ./pom.xml ./pom.xml

# copy components
COPY ./components ./components

# copy service
COPY ./service ./service

# install reactor modules
RUN mvn install

WORKDIR /service

# build service
RUN mvn package

# final base image
FROM openjdk:11-jre-slim

# set deployment directory
WORKDIR /mod-workflow

# copy over the built artifact from the maven image
COPY --from=maven /service/target/workflow-service*.jar ./mod-workflow.jar

# environment
ENV SERVER_PORT='9000'

# expose ports
EXPOSE ${SERVER_PORT}
EXPOSE 61616

RUN mkdir -p activemq-data

# run java command
CMD java -jar ./mod-workflow.jar
