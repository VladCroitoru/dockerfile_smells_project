FROM xcq1/steamcmd-rcon
LABEL maintainer="mail@tobiaskuhn.de"

# set inherited variables

ENV STEAMID "376030"
ENV INSTALLDIR "/home/steam/ark/game/"

ENV RCON_HOST "localhost"
ENV RCON_PORT "32330"
ENV RCON_PASSWORD ""
ENV RCON_HEALTH_COMMAND "listplayers"
ENV RCON_HEALTH_REGEXP "(No Players|[0-9]\.)"

# auto-fetch the rcon password from /home/steam/ark/rcon_pass
USER root
RUN sed -i 's|python|export RCON_PASSWORD=$(cat /home/steam/ark/rcon_pass)\n&|' /home/steam/rcon/healthcheck.sh

# Ark stuff

ENV SERVER_NAME ""
ENV MAP_NAME "TheIsland"
ENV MOD_LIST ""
ENV DIFFICULTY ""
ENV MAX_PLAYERS "70"
ENV BATTLE_EYE "true"
ENV RCON_GAME_LOG_BUFFER "100"
ENV WHITELIST_PLAYERS ""
ENV ADDITIONAL_SERVER_COMMAND_LINE ""
ENV AUTO_UPDATE "true"
ENV SAVE_GAME_NAME ""
ENV CLUSTER_NAME ""
ENV PORT "7777"
ENV RAWPORT "7778"
ENV QUERYPORT "27015"

EXPOSE $PORT/udp $RAWPORT/udp $QUERYPORT/udp 32330

VOLUME /home/steam/ark/game/ShooterGame/Saved
STOPSIGNAL SIGINT
WORKDIR /home/steam/ark/

ADD https://github.com/xcq1/ark-moddodo/archive/master.tar.gz /home/steam/ark/
RUN tar -xvzf /home/steam/ark/master.tar.gz && \
	rm /home/steam/ark/master.tar.gz && \
	chown -R steam:steam /home/steam/ark/ark-moddodo-master

ADD run.sh /home/steam/ark/run.sh
RUN chmod +x /home/steam/ark/run.sh && \
	chown -R steam:steam /home/steam/ark

ADD versioncheck/versioncheck.sh /home/steam/ark/versioncheck/versioncheck.sh
ADD versioncheck/playercheck.py /home/steam/ark/versioncheck/playercheck.py
ADD versioncheck/broadcast.py /home/steam/ark/versioncheck/broadcast.py
RUN chmod +x /home/steam/ark/versioncheck/*

RUN apt update && \
	apt install -y cron sudo python3 && \
	apt clean
ADD versioncheck/crontab /etc/cron.d/ark-cron
RUN chmod +x /etc/cron.d/ark-cron

# sudo so run.sh can start cron
RUN echo "steam   ALL=NOPASSWD:ALL" >> /etc/sudoers

USER steam

CMD ["/home/steam/ark/run.sh"]