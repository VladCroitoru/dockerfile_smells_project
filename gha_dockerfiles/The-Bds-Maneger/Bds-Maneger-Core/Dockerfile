# Setup Bds Manerger Project Docker Base
FROM debian:testing AS bdsbase
USER root
ENV DEBIAN_FRONTEND="noninteractive" DOCKER_IMAGE="true"

# Copy Docker Files
COPY .Build/Docker/* /tmp

# Configure BASE
RUN bash /tmp/Configure.sh

# Setup bdsmaneger/core
FROM bdsbase AS bdscore

# Create Volume to Storage Server And Config
VOLUME [ "/root/bds_core" ]

# Set default ENVs to Bds Core
ENV PLAYERS="5" \
    WORLD_NAME="The Ultimate Server" \
    DESCRIPTION="running Minecraft Server on Bds Maneger by Bds Manager Project" \
    GAMEMODE="survival" \
    DIFFICULTY="normal" \
    ENABLE_COMMANDS="false" \
    ACCOUNT="false" \
    SERVER="bedrock" \
    UPDATE_SERVER="true"

# Bds Maneger Core required ports
EXPOSE 19132/udp 19133/udp 1932/tcp

# Copy Bds Maneger Core
WORKDIR /opt/backend_core_scripts/

# Install Core dependencies
COPY package*.json ./
RUN npm install

# Copy BdsManger Core
COPY ./ ./
RUN chmod a+x -v bin/*

# Set Entrypint
ENTRYPOINT [ "node", "./bin/Docker.js" ]
