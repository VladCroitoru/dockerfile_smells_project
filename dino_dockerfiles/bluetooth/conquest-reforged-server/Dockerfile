FROM bluetooth/minecraft-server

MAINTAINER BlueTooth

CMD wget --output-document=forge-installer.jar https://files.minecraftforge.net/maven/net/minecraftforge/forge/1.10.2-12.18.3.2511/forge-1.10.2-12.18.3.2511-installer.jar && \
java -jar forge-installer.jar --installServer && \
java -Xmx4096M -Xms4096M -jar forge-1.10.2-12.18.3.2511-universal.jar nogui
