FROM maven:3-openjdk-11 as build
COPY $PWD /fhirspark
WORKDIR /fhirspark
RUN mvn -DskipTests clean package

FROM gcr.io/distroless/java-debian10:11
COPY --from=build /fhirspark/target/fhirspark-*-jar-with-dependencies.jar /app/fhirspark.jar
CMD ["/app/fhirspark.jar"]