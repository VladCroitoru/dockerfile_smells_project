FROM ibmjava:sfj-alpine

MAINTAINER dkraemer

RUN apk --no-cache add jq curl

RUN set -x \
  && addgroup -g 1000 minecraft \
  && adduser -u 1000 -D -G minecraft minecraft \
  && mkdir /data 

EXPOSE 25565 25575

ADD https://github.com/itzg/restify/releases/download/1.0.3/restify_linux_amd64 /usr/local/bin/restify
COPY start.sh /start
COPY server.properties /tmp/server.properties
RUN chmod +x /usr/local/bin/* /start \
  && chown -R minecraft:minecraft /data 

WORKDIR /data

CMD [ "/start" ]

ENV UID=1000 GID=1000 \
    MOTD="A Minecraft Server Powered by Docker" \
    JVM_OPTS="-Xmx1024M -Xms1024M" \
    TYPE=VANILLA VERSION=LATEST FORGEVERSION=RECOMMENDED LEVEL=world PVP=true DIFFICULTY=easy \
    LEVEL_TYPE=DEFAULT GENERATOR_SETTINGS= WORLD= MODPACK= ONLINE_MODE=TRUE
