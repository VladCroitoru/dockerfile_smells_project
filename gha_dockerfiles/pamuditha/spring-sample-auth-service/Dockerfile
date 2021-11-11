FROM maven:3.5.2-alpine as builder

WORKDIR /usr/src/app

# Copying `pom.xml` and installing dependencies makes this layer cachable.
# This will preven `mvn install` happening everytime a source file is changed.
# Only when the `pom.xml` is changed this will run `npm install` again.
COPY pom.xml .

RUN mvn compile

COPY src /usr/src/app/src

RUN mvn package

FROM openjdk:alpine

ENV PORT 8080

EXPOSE 8080

WORKDIR /usr/src/app

COPY --from=builder /usr/src/app/target/*.jar app.jar

ENTRYPOINT exec java $JAVA_OPTS -jar app.jar
