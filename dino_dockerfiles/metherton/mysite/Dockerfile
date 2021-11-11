FROM java:7

WORKDIR /home/root/mysite

COPY src /home/root/mysite/src
COPY pom.xml /home/root/mysite/pom.xml

RUN apt-get update && apt-get install -y maven
RUN mvn package

ENTRYPOINT ["mvn", "spring-boot:run"]
