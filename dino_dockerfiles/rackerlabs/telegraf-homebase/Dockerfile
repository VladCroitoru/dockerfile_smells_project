FROM maven:3.5.0-jdk-8 as build

WORKDIR /build
COPY pom.xml /build
RUN mvn dependency:go-offline

COPY . .
RUN mvn package

FROM openjdk:8-jre

WORKDIR /app
COPY --from=build /build/target/telegraf-homebase.jar /app/

EXPOSE 6565 8080

HEALTHCHECK --start-period=10s CMD ["/usr/bin/curl","http://localhost:8080/health"]

ENTRYPOINT ["/usr/bin/java"]
CMD ["-jar","/app/telegraf-homebase.jar"]