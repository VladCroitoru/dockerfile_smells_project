FROM ubuntu:16.04

MAINTAINER mdestombes

# Var for first config
# Server Name
ENV SESSIONNAME "ArkServer"
# Map name
ENV SERVERMAP "TheIsland"
# Server password
ENV SERVERPASSWORD "ServerPassword"
# Admin password
ENV ADMINPASSWORD "AdminPassword"
# Nb Players
ENV NBPLAYERS 20
# If the server is updating when start with docker start
ENV UPDATEONSTART 0
# if the server is backup when start with docker start
ENV BACKUPONSTART 0
#  Tag on github for ark server tools
ENV GIT_TAG v1.6.42
# Server PORT
ENV SERVERPORT 27015
# Steam port
ENV STEAMPORT 7778
# Rcon port
ENV RCONPORT 32330
# if the server should backup after stopping
ENV BACKUPONSTOP 0
# If the server warn the players before stopping
ENV WARNONSTOP 0
# Number of sub instance server
ENV NBINSTANCES 1

# Install dependencies
RUN apt-get update &&\
    apt-get dist-upgrade -y &&\
    apt-get install -y \
        bzip2 \
        curl \
        lib32gcc1 \
        libc6-i386 \
        lsof \
        git \
        nano \
        perl-modules

# Run commands as the steam user
RUN adduser \ 
	--disabled-login \ 
	--shell /bin/bash \ 
	--gecos "" \ 
	steam

# Add to sudo group
RUN usermod -a -G sudo steam

# Copy & rights to folders
COPY run.sh /home/steam/run.sh
COPY crontab /home/steam/crontab

#RUN touch /root/.bash_profile
RUN chmod 777 /home/steam/run.sh

# We use the git method, because api github has a limit ;)
RUN  git clone https://github.com/FezVrasta/ark-server-tools.git /home/steam/ark-server-tools
WORKDIR /home/steam/ark-server-tools/
RUN  git checkout $GIT_TAG 
# Install 
WORKDIR /home/steam/ark-server-tools/tools
RUN chmod +x install.sh 
RUN ./install.sh steam 

# Allow crontab to call arkmanager
RUN ln -s /usr/local/bin/arkmanager /usr/bin/arkmanager

# Define default config file in /etc/arkmanager
COPY arkmanager-system.cfg /tmp/arkmanager.cfg
COPY arkmanager-user.cfg /tmp/main_instance.cfg

# download steamcmd
RUN mkdir /home/steam/steamcmd &&\ 
	cd /home/steam/steamcmd &&\ 
	curl http://media.steampowered.com/installer/steamcmd_linux.tar.gz | tar -vxz 

EXPOSE ${STEAMPORT} 32330 ${SERVERPORT}
# Add UDP
EXPOSE ${STEAMPORT}/udp ${SERVERPORT}/udp

# Change the working directory to ARK
VOLUME  /home/steam/ARK
WORKDIR /home/steam/ARK

# Update game launch the game.
ENTRYPOINT ["/home/steam/run.sh"]
