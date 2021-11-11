FROM scratch
MAINTAINER "Ryan - faceless.saint@gmail.com"

# version information
ENV MINECRAFT_VERSION=1.7.10 \
        FORGE_VERSION=10.13.4.1448

# label containers for use with Hivemined
LABEL hivemined.comb hivemined.minecraft.version=${MINECRAFT_VERSION} hivemined.forge.version=${FORGE_VERSION}
ONBUILD LABEL hivemined.comb hivemined.minecraft.version=${MINECRAFT_VERSION} hivemined.forge.version=${FORGE_VERSION}

# copy local installation files
COPY ["src/", "/mnt/minecraft/"]

# specify volume location
VOLUME ["/mnt/minecraft"]
