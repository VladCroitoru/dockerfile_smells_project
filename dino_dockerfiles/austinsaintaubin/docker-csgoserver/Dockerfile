#
# CSGO Dockerfile
#
# https://hub.docker.com/r/austinsaintaubin/docker-csgoserver/
# Also see: https://hub.docker.com/r/johnjelinek/csgoserver/~/dockerfile/

# Pull the base image
FROM ubuntu:14.04
MAINTAINER Austin St. Aubin <AustinSaintAubin@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

#### Variables ####
ENV SERVER_NAME "Counter Strike: Global Offensive - Docker Server"
ENV RCON_PASS rconpass
ENV SERVER_PASS ""
ENV SERVER_LAN 0
ENV SERVER_REGION 0

# Notification Email
# (on|off)
ENV EMAIL_NOTIFICATION off
ENV EMAIL email@example.com

# STEAM LOGIN
ENV STEAM_USER anonymous
ENV STEAM_PASS ""

# Start Variables
# https://developer.valvesoftware.com/wiki/Counter-Strike:_Global_Offensive_Dedicated_Servers#Starting_the_Server
# [Game Modes]           gametype    gamemode
# Arms Race                  1            0
# Classic Casual             0            0
# Classic Competitive        0            1
# Demolition                 1            1
# Deathmatch                 1            2
ENV GAME_MODE 0
ENV GAME_TYPE 0
ENV DEFAULT_MAP de_dust2
ENV MAP_GROUP random_classic
ENV MAX_PLAYERS 16
ENV TICK_RATE 64
ENV GAME_PORT 27015
ENV SOURCE_TV_PORT 27020
ENV CLIENT_PORT 27005
ENV GAME_IP 0.0.0.0
ENV UPDATE_ON_START off

# Optional: Workshop Parameters
# https://developer.valvesoftware.com/wiki/CSGO_Workshop_For_Server_Operators
# To get an authkey visit - http://steamcommunity.com/dev/apikey
ENV AUTH_KEY ""
ENV WS_COLLECTION_ID ""
ENV WS_START_MAP ""

# Expose Ports
EXPOSE $GAME_PORT
EXPOSE $GAME_PORT/udp
EXPOSE $SOURCE_TV_PORT/udp
EXPOSE $CLIENT_PORT/udp
#EXPOSE 1200/udp

# Install Packages / Dependencies
RUN apt-get update -y && apt-get upgrade -y && \
    apt-get install -qqy wget nano tmux mailutils postfix lib32gcc1 \
                         gdb ca-certificates bsdmainutils
# Install Postfix Package OR https://hub.docker.com/r/catatnight/postfix/

# FIX ( perl: warning: Please check that your locale settings: )
# http://ubuntuforums.org/showthread.php?t=1346581
RUN locale-gen en_US en_US.UTF-8 hu_HU hu_HU.UTF-8
RUN dpkg-reconfigure locales

# # Cleanup
# RUN apt-get clean && \
#     rm -fr /var/lib/apt/lists/* && \
#     rm -fr /tmp/*

# Create softlink for script (Downloaded Later), this will allow ENTRYPOINT to find the script ( endpoint runs in /root/ )
# RUN ln -s "/home/csgoserver/csgoserver" "/root/csgoserver"

# Create user to run as
# script refuses to run in root, create user
RUN groupadd -r csgoserver && \
	useradd -rm -g csgoserver csgoserver && \
	adduser csgoserver sudo && \
	echo "csgoserver ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
USER csgoserver
WORKDIR /home/csgoserver

# Volume
RUN chown -R csgoserver:csgoserver /home/csgoserver
# VOLUME ["/home/csgoserver/serverfiles"]

# Download CSGO Server Manager Script
# https://raw.githubusercontent.com/dgibbs64/linuxgameservers/master/CounterStrikeGlobalOffensive/csgoserver
RUN wget http://gameservermanagers.com/dl/csgoserver && \
    chmod +x csgoserver

# Edit Server Script to hold Docker Environmental Varables
RUN sed -i '/emailnotification=/s/"\([^"]*\)"/"$EMAIL_NOTIFICATION"/' csgoserver && \
    sed -i '/email=/s/"\([^"]*\)"/"$EMAIL"/' csgoserver && \
    sed -i '/steamuser=/s/"\([^"]*\)"/"$STEAM_USER"/' csgoserver && \
    sed -i '/steampass=/s/"\([^"]*\)"/"$STEAM_PASS"/' csgoserver && \
    sed -i '/gamemode=/s/"\([^"]*\)"/"$GAME_MODE"/' csgoserver && \
    sed -i '/gametype=/s/"\([^"]*\)"/"$GAME_TYPE"/' csgoserver && \
    sed -i '/defaultmap=/s/"\([^"]*\)"/"$DEFAULT_MAP"/' csgoserver && \
    sed -i '/mapgroup=/s/"\([^"]*\)"/"$MAP_GROUP"/' csgoserver && \
    sed -i '/maxplayers=/s/"\([^"]*\)"/"$MAX_PLAYERS"/' csgoserver && \
    sed -i '/tickrate=/s/"\([^"]*\)"/"$TICK_RATE"/' csgoserver && \
    sed -i '/port=/s/"\([^"]*\)"/"$GAME_PORT"/' csgoserver && \
    sed -i '/sourcetvport=/s/"\([^"]*\)"/"$SOURCE_TV_PORT"/' csgoserver && \
    sed -i '/clientport=/s/"\([^"]*\)"/"$CLIENT_PORT"/' csgoserver && \
    sed -i '/ip=/s/"\([^"]*\)"/"$GAME_IP"/' csgoserver && \
    sed -i '/updateonstart=/s/"\([^"]*\)"/"$UPDATE_ON_START"/' csgoserver && \
    sed -i '/authkey=/s/"\([^"]*\)"/"$AUTH_KEY"/' csgoserver && \
    sed -i '/ws_collection_id=/s/"\([^"]*\)"/"$WS_COLLECTION_ID"/' csgoserver && \
    sed -i '/ws_start_map=/s/"\([^"]*\)"/"$WS_START_MAP"/' csgoserver
# RUN cat csgoserver  # DEBUG

# Run Install Script
# RUN ./csgoserver auto-install

# Make Start Script
RUN echo '# Docker Start / Run Script' > start.sh && \
    echo '' >> start.sh && \
    echo '# Edit Server Config to hold Docker Environmental Varables' >> start.sh && \
    echo '# ------------------' >> start.sh && \
    echo 'sed -i "/hostname/s/\"\([^\"]*\)\"/\"$SERVER_NAME\"/" serverfiles/csgo/cfg/csgo-server.cfg' >> start.sh && \
    echo 'sed -i "/rcon_password/s/\"\([^\"]*\)\"/\"$RCON_PASS\"/" serverfiles/csgo/cfg/csgo-server.cfg' >> start.sh && \
    echo 'sed -i "/sv_password/s/\"\([^\"]*\)\"/\"$SERVER_PASS\"/" serverfiles/csgo/cfg/csgo-server.cfg' >> start.sh && \
    echo 'sed -i "/sv_lan/s/\"\([^\"]*\)\"/\"$SERVER_LAN\"/" serverfiles/csgo/cfg/csgo-server.cfg' >> start.sh && \
    echo 'sed -i "/sv_region/s/\"\([^\"]*\)\"/\"$SERVER_REGION\"/" serverfiles/csgo/cfg/csgo-server.cfg' >> start.sh && \
    echo 'sed -i '\''s/""/"/g'\'' serverfiles/csgo/cfg/csgo-server.cfg' >> start.sh && \
    echo '# ------------------' >> start.sh && \
    echo '' >> start.sh && \
    echo '# Script Manager' >> start.sh && \
#     echo './csgoserver auto-install' >> start.sh && \
#     echo './csgoserver update' >> start.sh && \
#     echo './csgoserver details' >> start.sh && \
    echo './csgoserver' >> start.sh && \
    echo './csgoserver start' >> start.sh && \
    chmod +x start.sh

# Make Steam 1st time Autentiaction (used to setup cached cradentuals for accounts with 2 factor authentication)
RUN echo '# Steam 1st time Autentiaction (used to setup cached cradentuals for accounts with 2 factor authentication)' > steam-login.sh && \
    echo '# ------------------' >> steam-login.sh && \
    echo 'echo Before running this script you might have to run "./csgoserver install" to download "steamcmd"' >> steam-login.sh && \
    echo 'echo After running this script, edit "csgoserver" script or the "STEAM_PASS" envirmental varable and clear out the password with a space or leave it blank' >> steam-login.sh && \
    echo 'echo =================' >> steam-login.sh && \
    #echo 'echo enter password & 2nd factor' >> start.sh && \
    echo 'steamcmd/./steamcmd.sh +login $STEAM_USER $STEAM_PASS  # Login to steam' >> steam-login.sh && \
    echo 'sed -i "/steampass=/s/\"\([^\"]*\)\"/\"\"/" csgoserver  # CLEAR PASSWORD FIELD in csgoserver script' >> steam-login.sh && \
    chmod +x steam-login.sh

# Run Start Script
# https://labs.ctl.io/dockerfile-entrypoint-vs-cmd/
# http://stackoverflow.com/questions/21553353/what-is-the-difference-between-cmd-and-entrypoint-in-a-dockerfile
# http://kimh.github.io/blog/en/docker/gotchas-in-writing-dockerfile-en/
# http://www.markbetz.net/2014/03/17/docker-run-startup-scripts-then-exit-to-a-shell/
# http://crosbymichael.com/dockerfile-best-practices.html
# https://blog.phusion.nl/2015/01/20/docker-and-the-pid-1-zombie-reaping-problem/
# ENTRYPOINT ["./csgoserver"]  # does not work the way I want to.
# CMD ["/bin/bash", "-c", "set -e && /home/csgoserver/start.sh"]  # DOES NOT STAY RUNNING.
CMD bash -c 'exec /home/csgoserver/start.sh';'bash'