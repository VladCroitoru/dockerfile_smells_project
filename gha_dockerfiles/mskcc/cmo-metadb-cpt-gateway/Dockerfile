FROM maven:3.6.1-jdk-8-slim
# create working directory and set
RUN mkdir /cpt-gateway
ADD . /cpt-gateway
WORKDIR /cpt-gateway
RUN mvn clean install

# copy jar and set entrypoint
FROM openjdk:8-slim
COPY --from=0 /cpt-gateway/server/target/cmo_metadb_cpt_gateway.jar /cpt-gateway/cmo_metadb_cpt_gateway.jar
ENTRYPOINT ["java"]
