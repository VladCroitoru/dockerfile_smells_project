# Dockerfile that uses the jar file to dockerize
FROM maven:3.2-jdk-7-onbuild
CMD ["java","-jar","/usr/src/app/target/dropwizard-example-1.0-SNAPSHOT.jar","server","configuration.yml"]
EXPOSE 8080