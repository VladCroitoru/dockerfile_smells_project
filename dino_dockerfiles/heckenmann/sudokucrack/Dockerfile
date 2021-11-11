FROM maven:3.5.3-jdk-8-alpine as build
COPY src/ /tmp/src
COPY pom.xml /tmp/pom.xml
WORKDIR /tmp
RUN mvn clean install


FROM openjdk:8-jre-alpine
EXPOSE 8080
RUN mkdir -p /opt/sc
COPY --from=build /tmp/target/sudokucrack-swarm.jar /opt/sc/sudokucrack-swarm.jar
CMD java -jar /opt/sc/sudokucrack-swarm.jar -Djava.net.preferIPv4Stack=true