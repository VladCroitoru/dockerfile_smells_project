FROM maven:3.6.1-jdk-8-slim
RUN mkdir /request-filter
ADD . /request-filter
WORKDIR /request-filter
RUN mvn clean install

FROM openjdk:8-slim
COPY --from=0 /request-filter/target/cmo_metadb_request_filter.jar /request-filter/cmo_metadb_request_filter.jar
ENTRYPOINT ["java"]
