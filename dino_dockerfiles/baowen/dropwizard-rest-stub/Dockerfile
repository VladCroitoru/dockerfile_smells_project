FROM maven:3.5.0-jdk-8-alpine as builder
WORKDIR /var/app
COPY . /var/app
RUN mvn install
RUN cd /var/app/target && ls -ltr


FROM openjdk:8u121-jre-alpine
MAINTAINER Ben Owen http://benaowen.com/
WORKDIR /var/dropwizard-rest-stub
COPY --from=builder /var/app/target/dropwizard-rest-stub-1.0-SNAPSHOT.jar /var/dropwizard-rest-stub/dropwizard-rest-stub.jar
ADD config-docker.yml /var/dropwizard-rest-stub/config.yml
EXPOSE 9000 9001
ENTRYPOINT ["java", "-jar", "dropwizard-rest-stub.jar", "server", "config.yml"]