
FROM maven:3.8.3-jdk-11-slim as BUILD_IMAGE

RUN mkdir -p /home/
COPY pom.xml /home/
COPY src /home/src
COPY .git /home/.git

WORKDIR /home/
RUN mvn --file /home/pom.xml clean install package


FROM openjdk:11-jre-slim

COPY --from=BUILD_IMAGE /home/target/bbs-backend*.jar ./bbs-backend.jar
ENTRYPOINT java -jar bbs-backend.jar

VOLUME /var/lib/bbs-backend.jar/config
EXPOSE 8079
