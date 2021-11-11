FROM java:8

# Install maven
RUN apt-get update && apt-get install -y maven

WORKDIR /code

# Prepare by downloading dependencies
ADD pom.xml /code/pom.xml
RUN ["mvn", "dependency:resolve"]
RUN ["mvn", "verify"]

# Adding source, compile and package into a fat jar
ADD src /code/src
RUN ["mvn", "install"]
RUN ["mvn", "package"]

EXPOSE 80
CMD ["/usr/lib/jvm/java-8-openjdk-amd64/bin/java", "-jar", "target/sparkapi-1.0.jar"]
