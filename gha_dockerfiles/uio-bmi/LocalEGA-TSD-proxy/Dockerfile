FROM maven:3.6.1-jdk-13-alpine as builder

COPY pom.xml .

RUN mvn dependency:go-offline --no-transfer-progress

COPY src/ /src/

RUN mvn clean install -DskipTests --no-transfer-progress

FROM openjdk:13-alpine

RUN apk add --no-cache ca-certificates

COPY --from=builder /target/*-SNAPSHOT.jar /localega-tsd-proxy.jar

RUN addgroup -g 1000 lega && \
    adduser -D -u 1000 -G lega lega

USER 1000

CMD ["java", "-jar", "/localega-tsd-proxy.jar"]
