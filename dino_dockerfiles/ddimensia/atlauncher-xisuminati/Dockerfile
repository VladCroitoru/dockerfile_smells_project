FROM isuper/java-oracle:latest

MAINTAINER ddimensia

ENV SERVER_MAXHEAP 2048M
ENV SERVER_MINHEAP 512M
ENV SERVER_OPTS nogui

VOLUME ["/opt/minecraft/data"]

ADD rootfs/opt/minecraft /opt/minecraft

RUN apt-get update && apt-get install unzip
RUN curl --silent -o /opt/minecraft/minecraft_server.1.7.10.jar 'http://s3.amazonaws.com/Minecraft.Download/versions/1.7.10/minecraft_server.1.7.10.jar'
RUN curl --silent -o /tmp/server.zip "`curl --silent 'https://www.atlauncher.com/pack/Xisuminati' | grep "Download Server" | sed 's/.*href="\([^"]*\)".*/\1/'`" && cd /opt/minecraft && unzip /tmp/server.zip && rm /tmp/server.zip

EXPOSE 25565

WORKDIR /opt/minecraft/data
CMD ["../server.sh"]



