# syntax=docker/dockerfile:experimental
FROM maven:3.8.2-jdk-11-slim AS builder

WORKDIR /app
COPY src src/
COPY pom.xml .

# mvn clean install ( e criando o cache para .m2 )
RUN --mount=type=cache,target=/root/.m2 \
	mvn clean package -DskipTests && \
    cp target/*.jar target/app.jar

# mvn clean install ( sem cache para .m2 )
#RUN mvn clean package -DskipTests &&  cp target/*.jar target/app.jar

FROM openjdk:11.0.12-jre-slim

RUN apt-get update -y && apt-get install -y --no-install-recommends \
	curl  \
	jq  \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace
COPY --from=builder /app/target/app.jar .
CMD [ "java", "-jar", "app.jar" ]
