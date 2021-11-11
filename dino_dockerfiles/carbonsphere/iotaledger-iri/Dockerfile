############################################################
# If this docker container helps you in anyway
# please consider making a donation to the following address
# IOTA: IGTKRHHTOIAHB9HCYIZNLPASKHEENKIJICZCCJSUXNZGFKYRLNOJQ9TMXIJYFUBLQ9YWXRMSMWXNDQWD9QINXNXOXW
# ETH: 0xb205a4560bbc9840b80d36245333401e65d4f05e
# BTC: 395vsb41m46voFyhrgYMh6TauWKmNqJAtm
# Thanks!
############################################################

FROM maven:3.5-jdk-8 as builder
WORKDIR /iri
RUN git clone https://github.com/iotaledger/iri /iri
RUN mvn clean package

FROM openjdk:jre-slim
WORKDIR /iri
COPY --from=builder /iri/target/iri-*.jar /iri
COPY --from=builder /iri/logback.xml /iri
COPY iota.ini /iri
COPY docker-entrypoint.sh /

ENV MAX_MEMORY 4G
ENV MIN_MEMORY 1G

ENV REMOTE_LIMIT_API "attachToTangle"

ENV API_PORT 14265
ENV UDP_PORT 14666
ENV TCP_PORT 15666

EXPOSE $API_PORT
EXPOSE $UDP_PORT/udp
EXPOSE $TCP_PORT

ENTRYPOINT ["/docker-entrypoint.sh"]
