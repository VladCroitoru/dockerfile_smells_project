FROM feedthebeast/ftbbase

ARG DOWNLOAD_URL=https://ftb.cursecdn.com/FTB2/modpacks/FTBPresentsDirewolf20112/1_9_0/FTBPresentsDirewolf20112Server.zip
ARG ZIP_NAME=direwolf20.zip
ARG DYNMAP_URL=https://minecraft.curseforge.com/projects/dynmapforge/files/2436596/download

COPY setup.sh ./
RUN /bin/bash setup.sh && \
    rm setup.sh

WORKDIR /home/minecraft/mcmyadmin
