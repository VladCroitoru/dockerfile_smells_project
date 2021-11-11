FROM jamesdbloom/docker-java8-maven

# Install maven
RUN apt-get update  
RUN apt-get install -y git

RUN git clone https://github.com/mmedum/WorksOnMyMachine /code

WORKDIR /code

# Prepare by downloading dependencies
CMD ["mvn", "dependency:resolve"]  
RUN ["mvn", "verify"]

# Adding source, compile and package into a fat jar
RUN ["mvn", "package"]

RUN ["java", "-version"]

RUN ["cp", "/code/target/WorksOnMyMachine-0.1-SNAPSHOT-jar-with-dependencies.jar", "/WorksOnMyMachine-0.1-SNAPSHOT-jar-with-dependencies.jar"]

ENTRYPOINT ["java", "-jar", "/WorksOnMyMachine-0.1-SNAPSHOT-jar-with-dependencies.jar"]

EXPOSE 8080
