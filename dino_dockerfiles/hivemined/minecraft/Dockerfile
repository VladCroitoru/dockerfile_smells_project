FROM scratch
MAINTAINER "Ryan - faceless.saint@gmail.com"

# version information
ENV MINECRAFT_VERSION=1.8.8

# label containers for use with Hivemined
LABEL hivemined.comb hivemined.minecraft.version=${MINECRAFT_VERSION}
ONBUILD LABEL hivemined.comb hivemined.minecraft.version=${MINECRAFT_VERSION}

# download server from official sources
ADD ["https://s3.amazonaws.com/Minecraft.Download/versions/${MINECRAFT_VERSION}/minecraft_server.${MINECRAFT_VERSION}.jar", \
        "/mnt/minecraft/"]

#specify volume location
VOLUME ["/mnt/minecraft"]

