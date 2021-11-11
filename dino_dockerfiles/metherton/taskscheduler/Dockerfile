FROM java:7

WORKDIR /home/root/taskscheduler

COPY src /home/root/taskscheduler/src
COPY pom.xml /home/root/taskscheduler/pom.xml

RUN apt-get update && apt-get install -y maven
RUN mvn package

ENTRYPOINT ["java", "-jar", "target/taskscheduler-0.0.1-SNAPSHOT.jar"]
