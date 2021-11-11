FROM maven:3.6.1-jdk-8-slim
RUN mkdir /cmo-metadb
ADD . /cmo-metadb
WORKDIR /cmo-metadb
RUN mvn clean install -DskipTests

FROM openjdk:8-slim
COPY --from=0 /cmo-metadb/server/target/cmo_metadb_server.jar /cmo-metadb/cmo_metadb_server.jar
ENTRYPOINT ["java"]
