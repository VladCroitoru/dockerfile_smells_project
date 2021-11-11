FROM java:7

WORKDIR /home/root/site

COPY src /home/root/site/src
COPY pom.xml /home/root/site/pom.xml

RUN apt-get update && apt-get install -y maven
RUN mvn package

ENTRYPOINT ["mvn", "spring-boot:run"]
