FROM java:7

WORKDIR /home/root/twilioappserver

COPY src /home/root/twilioappserver/src
COPY pom.xml /home/root/twilioappserver/pom.xml

RUN apt-get update && apt-get install -y maven
RUN mvn package

ENTRYPOINT ["java", "-jar", "target/twilioappserver-0.0.1-SNAPSHOT.jar"]
