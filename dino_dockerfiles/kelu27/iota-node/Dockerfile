FROM openjdk:8-jre-slim

LABEL maintainer="luc@charpentier.cloud"

WORKDIR /iri

RUN apt-get update && apt-get install -y \
    wget \
	--no-install-recommends \
	&& rm -rf /var/lib/apt/lists/* && \
    wget https://github.com/iotaledger/iri/releases/download/v1.3.2.2/iri-1.3.2.2.jar

COPY conf /iri/conf
COPY docker-entrypoint.sh /

VOLUME /iri/data

EXPOSE 14265
EXPOSE 14777/udp
EXPOSE 15777

WORKDIR /iri/data

ENTRYPOINT ["/docker-entrypoint.sh"]
