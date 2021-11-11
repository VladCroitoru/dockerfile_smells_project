# Minecraft - Bedrock Edition Image Build

FROM debian:buster

LABEL maintainer="Geoffrey Harrison <geoffh1977@gmail.com>"

ARG VERSION=1.17.34.02

# hadolint ignore=DL3008
RUN export DEBIAN_FRONTEND=noninteractive && \
  apt-get update && \
  apt-get install -y --no-install-recommends unzip curl libcurl4 libssl1.1 ca-certificates && \
  curl https://minecraft.azureedge.net/bin-linux/bedrock-server-${VERSION}.zip --output bedrock-server.zip && \
  unzip bedrock-server.zip -d bedrock-server && \
  rm bedrock-server.zip && \
  apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /bedrock-server

RUN mkdir config worlds && \
  mv permissions.json server.properties whitelist.json config/ && \
  ln -s /bedrock-server/config/permissions.json . && \
  ln -s /bedrock-server/config/server.properties . && \
  ln -s /bedrock-server/config/whitelist.json .

RUN useradd --create-home --shell /bin/bash minecraft && \
  chown minecraft:minecraft -R /bedrock-server

VOLUME ["/bedrock-server/config", "/bedrock-server/worlds"]

EXPOSE 19132/udp

USER minecraft

ENV LD_LIBRARY_PATH=.
CMD ["/bedrock-server/bedrock_server"]
