FROM ubuntu:20.04

# Base setuo was taken from
#https://github.com/TuRz4m/Ark-docker
MAINTAINER bigdaddymccarron

# Var for first config
# Arkmanager Branch
ENV BRANCH=master
# Set Terminal
ENV TERM=xterm
# Time Zone
ENV TZ=EST
# Server Name
ENV SESSIONNAME "Ark Docker"
# Map name
ENV SERVERMAP "TheIsland"
# Server password
ENV SERVERPASSWORD ""
# Admin password
ENV ADMINPASSWORD "adminpassword"
# Nb Players
ENV NBPLAYERS 32
# Game Mod list
ENV SERVERMODS ""
# If the server is updating when start with docker start
ENV UPDATEONSTART 1
# if the server is backup when start with docker start
ENV BACKUPONSTART 1
# Server PORT (you can't remap with docker, it doesn't work)
ENV SERVERPORT 7778
# Steam port (you can't remap with docker, it doesn't work)
ENV QUERYPORT 27015
# Remote Console port (you can't remap with docker, it doesn't work)
ENV RCONPORT 32330
# if the server should backup after stopping
ENV BACKUPONSTOP 1
# If the server warn the players before stopping
ENV WARNONSTOP 1
# UID of the user steam
ENV UID 1007
# GID of the user steam
ENV GID 281


# Install dependencies 
COPY sources.list /etc/apt/sources.list
RUN apt-get update &&\ 
    apt-get install -y curl lib32gcc1 lsof git vim sudo cron apt-utils
RUN DEBIAN_FRONTEND="noninteractive" apt-get install -y tzdata

# Enable passwordless sudo for users under the "sudo" group
COPY sudoers /etc/sudoers
RUN sed -i.bkp -e \
	's/%sudo\s\+ALL=(ALL\(:ALL\)\?)\s\+ALL/%sudo ALL=NOPASSWD:ALL/g' /etc/sudoers \
	/etc/sudoers

RUN echo '*	soft	nofile	100000' >> /etc/security/limits.conf
RUN echo '*	hard	nofile	100000' >> /etc/security/limits.conf
RUN echo 'root	soft	nofile	100000' >> /etc/security/limits.conf
RUN echo 'root	hard	nofile	100000' >> /etc/security/limits.conf

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
COPY user.sh /home/steam/user.sh
COPY crontab /home/steam/crontab
COPY arkmanager-user.cfg /home/steam/arkmanager.cfg
COPY arkshortcut.sh /usr/local/bin

RUN touch /root/.bash_profile
RUN chmod 755 /home/steam/run.sh
RUN chmod 755 /home/steam/user.sh
RUN chmod 755 /usr/local/bin/arkshortcut.sh
RUN mkdir  /ark
RUN mkdir  /root/Steam

WORKDIR /home/steam/
# We use the git method, because api github has a limit ;)
RUN  git clone https://github.com/arkmanager/ark-server-tools.git ark-server-tools

WORKDIR /home/steam/ark-server-tools/
# Install 
WORKDIR /home/steam/ark-server-tools/tools
RUN chmod +x install.sh 
RUN ./install.sh steam 

# Allow crontab to call arkmanager
RUN ln -s /usr/local/bin/arkmanager /usr/bin/arkmanager

# Create arkmanager shortcuts
RUN ln -s /usr/local/bin/arkshortcut.sh /usr/local/bin/status
RUN ln -s /usr/local/bin/arkshortcut.sh /usr/local/bin/start
RUN ln -s /usr/local/bin/arkshortcut.sh /usr/local/bin/stop
RUN ln -s /usr/local/bin/arkshortcut.sh /usr/local/bin/restart
RUN ln -s /usr/local/bin/arkshortcut.sh /usr/local/bin/update
RUN ln -s /usr/local/bin/arkshortcut.sh /usr/local/bin/updatemods
RUN ln -s /usr/local/bin/arkshortcut.sh /usr/local/bin/upgradetools
RUN ln -s /usr/local/bin/arkshortcut.sh /usr/local/bin/saveworld

# Define default config file in /etc/arkmanager
COPY arkmanager-system.cfg /etc/arkmanager/arkmanager.cfg

# Define default config file in /etc/arkmanager
COPY instance.cfg /etc/arkmanager/instances/main.cfg

RUN chown steam -R /ark && chmod 755 -R /ark
RUN chown steam -R /etc/arkmanager && chmod 755 -R /etc/arkmanager

# download steamcmd
RUN mkdir /home/steam/steamcmd &&\ 
	cd /home/steam/steamcmd &&\ 
	curl http://media.steampowered.com/installer/steamcmd_linux.tar.gz | tar -vxz 


EXPOSE ${QUERYPORT} ${SERVERPORT} 7777
EXPOSE ${QUERYPORT}/udp ${SERVERPORT}/udp 7777/udp
EXPOSE ${RCONPORT}/tcp

VOLUME  /ark 
VOLUME  /root/Steam 

# Change the working directory to /ark
WORKDIR /ark

# Update game launch the game.
ENTRYPOINT ["/home/steam/user.sh"]
