FROM java:7

WORKDIR /home/root/site/server

COPY src /home/root/site/server/src
COPY pom.xml /home/root/site/server/pom.xml

RUN apt-get update && apt-get install -y maven
RUN mvn package

ENTRYPOINT ["java", "-jar", "target/demo-0.0.1-SNAPSHOT.jar"]

