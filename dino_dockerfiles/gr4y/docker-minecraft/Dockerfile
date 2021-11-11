# Minecraft 1.12

FROM gr4y/docker-java8
LABEL maintainer="swessel+dockerhub@gr4yweb.de"

# Update System
RUN apt-get -y update && apt-get -y upgrade

ENV MC_VERSION 1.12.2
ENV SHA 886945bfb2b978778c3a0288fd7fab09d315b25f

# Download Minecraft Server
RUN wget -q https://launcher.mojang.com/mc/game/$MC_VERSION/server/$SHA/server.jar

# Accept Mojang EULA
RUN echo eula=true > eula.txt

WORKDIR /data
VOLUME /data

EXPOSE 25565

# Run minecraft.service
CMD java -Xmx2048M -jar /server.jar nogui
