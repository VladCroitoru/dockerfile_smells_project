# build the Spring project into a jar file
FROM openjdk:11-jdk-slim-buster as builder
RUN mkdir src
COPY . /src
WORKDIR /src
RUN chmod 755 mvnw && ./mvnw clean install -DskipTests


# Run the jar file from previous build
FROM openjdk:11-jdk-buster
EXPOSE 8080

RUN apt-get update -y && apt-get install -y wait-for-it

COPY --from=builder /src/target /build
WORKDIR /build

RUN groupadd -r spring && useradd --no-log-init -r -g spring spring
USER spring:spring

CMD ["java","-jar","register-backend.jar"]
