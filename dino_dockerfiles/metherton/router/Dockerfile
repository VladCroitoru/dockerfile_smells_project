FROM java:7

WORKDIR /home/root/router

COPY src /home/root/router/src
COPY pom.xml /home/root/router/pom.xml

RUN apt-get update && apt-get install -y maven
RUN mvn package

ENTRYPOINT ["mvn", "spring-boot:run"]
