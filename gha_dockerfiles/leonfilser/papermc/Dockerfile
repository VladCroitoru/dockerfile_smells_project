FROM openjdk:16-slim

MAINTAINER Leon Filser <leon.filser@gmail.com>

ENV DIR=/minecraft

ENV VERSION=latest
ENV XMS=4G
ENV XMX=8G

RUN mkdir ${DIR}
WORKDIR ${DIR}

COPY ./entrypoint.sh ${DIR}

RUN apt-get update && apt-get install wget jq -y \
    && rm -rf /var/lib/apt/lists

ENTRYPOINT ["sh", "entrypoint.sh"]

EXPOSE 25565/tcp
EXPOSE 25565/udp
