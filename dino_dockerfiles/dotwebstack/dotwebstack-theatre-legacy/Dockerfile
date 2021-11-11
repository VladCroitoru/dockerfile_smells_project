FROM maven:3.5-jdk-8-onbuild as builder

FROM openjdk:8-jre

COPY --from=builder /usr/src/app/target/dotwebstack-theatre-legacy*.jar /opt/dotwebstack-theatre-legacy.jar

WORKDIR /opt

CMD ["java","-jar","/opt/dotwebstack-theatre-legacy.jar"]

EXPOSE 8080
