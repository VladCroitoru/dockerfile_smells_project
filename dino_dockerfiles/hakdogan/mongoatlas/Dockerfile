FROM maven:3-jdk-8-alpine as build

COPY pom.xml /atlas/pom.xml
COPY src/ /atlas/src/

RUN mvn clean install -f /atlas/pom.xml

FROM openjdk:8-jre-alpine

COPY --from=build /atlas/target/mongoAtlas-1.0-SNAPSHOT.jar /atlas.jar

LABEL maintainer = "Hüseyin Akdoğan <huseyin.akdogan@kodcu.com>"

VOLUME /var/log

EXPOSE 8080

CMD ["sh","-c", "java -Dnetworkaddress.cache.ttl=60 -jar /atlas.jar"]