FROM maven:3.5-jdk-8-onbuild as builder

FROM openjdk:8-jre

COPY --from=builder /usr/src/app/target/dotwebstack-theatre*.jar /opt/dotwebstack-theatre.jar

WORKDIR /opt

CMD ["java","-jar","/opt/dotwebstack-theatre.jar"]

EXPOSE 8080
