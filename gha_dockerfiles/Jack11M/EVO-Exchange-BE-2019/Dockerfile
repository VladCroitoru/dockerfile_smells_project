FROM maven:3.8.1-openjdk-17-slim
COPY pom.xml /tmp/
COPY src /tmp/src/
WORKDIR /tmp/
RUN mvn clean install