FROM java:7-jre

MAINTAINER Code Hz

ENV SCREEN_NAME MinecraftForgeServer
ENV MCSERVER_PATH /srv/minecraft
ENV MINECRAFT_VERSION 1.6.4
ENV MCFORGE_VERSION 9.11.1.1345
ENV MCFORGE_INSTALLER_JAR forge-installer.jar

ENV JAVA_XMX 1G
ENV JAVA_XMS 1G
ENV JAVA_PERMSIZE 455m

ENV MINECRAFT_OPTS "-server -Xmx$JAVA_XMX -Xms$JAVA_XMS -XX:MaxPermSize=$JAVA_PERMSIZE -XX:+UseParNewGC -XX:+UseConcMarkSweepGC"

ENV MINECRAFT_EULA false
ENV DEFAULT_OP CodeHz

ENV GENERATOR_SETTINGS ""
ENV OP_PERMISSION_LEVEL 4
ENV ALLOW_NETHER true
ENV LEVEL_NAME world
ENV ENABLE_QUERY true
ENV ALLOW_FLIGHT true
ENV ANNOUNCE_PLAYER_ACHIEVEMENTS true
ENV SERVER_PORT 25565
ENV LEVEL_TYPE default
ENV ENABLE_RCON true
ENV RCON_PASSWORD 12345678
ENV RCON_PORT 25575
ENV FORCE_GAMEMODE false
ENV LEVEL_SEED ""
ENV SERVER_IP 0.0.0.0
ENV MAX_BUILD_HEIGHT 256
ENV SPAWN_NPCS true
ENV WHITE_LIST false
ENV SPAWN_ANIMALS true
ENV SNOOPER_ENABLED true
ENV ONLINE_MODE true
ENV RESOURCE_PACK ""
ENV PVP true
ENV DIFFICULTY 2
ENV ENABLE_COMMAND_BLOCK true
ENV PLAYER_IDLE_TIMEOUT 0
ENV GAMEMODE 0
ENV MAX_PLAYERS 20
ENV SPAWN_MONSTERS true
ENV VIEW_DISTANCE 10
ENV GENERATE_STRUCTURES true

RUN gpg --keyserver pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4
RUN apt-get update && apt-get install -y curl screen && rm -rf /var/lib/apt/lists/* \
    && curl -o /usr/local/bin/gosu -SL "https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-architecture)" \
    && curl -o /usr/local/bin/gosu.asc -SL "https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-architecture).asc" \
    && gpg --verify /usr/local/bin/gosu.asc \
    && rm /usr/local/bin/gosu.asc \
    && chmod +x /usr/local/bin/gosu

RUN \
    groupadd -g 1000 minecraft && \
    useradd -g minecraft -u 1000 -r -M minecraft

RUN mkdir -p $MCSERVER_PATH && mkdir -p /srv/minecraft-bin

VOLUME ["$MCSERVER_PATH"]

WORKDIR /srv/minecraft-bin
COPY minecraft /usr/local/bin/
RUN chmod +x /usr/local/bin/minecraft && /usr/local/bin/minecraft install

EXPOSE $SERVER_PORT
EXPOSE $RCON_PORT

WORKDIR $MCSERVER_PATH

CMD ["minecraft", "run"]
