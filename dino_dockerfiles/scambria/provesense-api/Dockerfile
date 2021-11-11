FROM maven:3.3-jdk-8

WORKDIR /code

# Prepare by downloading dependencies
ADD pom.xml /code/pom.xml
RUN ["mvn", "dependency:resolve"]
RUN ["mvn", "verify"]

# Adding source, compile and package into a fat jar
ADD src /code/src

RUN ["mvn", "install"]

EXPOSE 4567
CMD ["/usr/lib/jvm/java-8-openjdk-amd64/bin/java", "-jar", "target/provesense-api-jar-with-dependencies.jar"]
