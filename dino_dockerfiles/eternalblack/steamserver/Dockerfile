FROM debian:jessie
MAINTAINER Markus Bittner <Bittner@EternalBlack.com>

ENV APPID=4020 \
    MAP=gm_construct \
    GAME_TYPE=garrysmod \
    WORKSHOP_KEY= \
    WORKSHOP_ID= \
    GAME_MODE=Sandbox \
    MAX_PLAYERS=64

ADD . /docker

USER root
RUN apt-get update && apt-get install -y lib32gcc1 lib32stdc++6 wget
RUN chmod +x /docker/install_steamcmd.sh && chmod +x /docker/exec_install.sh && useradd -m steam
RUN mkdir -p /home/steam/garrysmod
RUN chown steam:steam /home/steam -R
USER steam

VOLUME /home/steam/garrysmod
VOLUME /home/steam/tf2
VOLUME /home/steam/css
EXPOSE 27015 27015/udp

ENTRYPOINT ["/docker/exec_install.sh"]
