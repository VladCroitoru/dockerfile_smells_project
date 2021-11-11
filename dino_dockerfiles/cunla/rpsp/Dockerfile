FROM java:8

# Install maven
RUN apt-get update
RUN apt-get install -y maven

ADD fapi-client-4.3.jar /
RUN ["mvn", "install:install-file", "-Dfile=fapi-client-4.3.jar", "-DgroupId=com.emc" ,"-DartifactId=fapi-client" ,"-Dversion=4.3" ,"-Dpackaging=jar"]
WORKDIR /code

# Prepare by downloading dependencies
ADD pom.xml /code/pom.xml

# Adding source, compile and package into a fat jar
ADD src /code/src
RUN ["mvn", "dependency:resolve"]
RUN ["mvn", "verify"]
RUN ["mvn", "package"]

EXPOSE 4567
CMD ["/usr/lib/jvm/java-8-openjdk-amd64/bin/java", "-Xms512m", "-Xmx1g", "-jar", "target/rpsp.war"]
