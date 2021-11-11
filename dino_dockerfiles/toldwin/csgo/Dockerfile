FROM ubuntu 
MAINTAINER Toldwin <toldwin@gmail.com> 

ENV REFRESH_DATE=2020/06/11

# lib32gcc1 installation 
RUN \ 
  apt-get update && \ 
  DEBIAN_FRONTEND=noninteractive && \ 
  apt-get -y install lib32gcc1 && \ 
  apt-get -y install wget 

# Steam installation 
RUN mkdir /steamcmd && \ 
    cd /steamcmd && \ 
        wget http://media.steampowered.com/installer/steamcmd_linux.tar.gz && \ 
        tar -xvzf steamcmd_linux.tar.gz 

# CSGO dedicated server installation 
RUN /steamcmd/steamcmd.sh +login anonymous +force_install_dir /steamcmd/csgoserver +app_update 740 validate +quit 

# Steam user creation and usage 
#RUN useradd -m steam --password password 
#RUN sudo chown -R steam: /steamcmd 
#user steam 

# Expose Dedicated server port 
EXPOSE 27015/udp

# Add conf file including root password
ADD server.cfg /steamcmd/csgoserver/csgo/cfg/server.cfg
        
# Used Dedicated server parameters 
ENV GAME_TYPE 0 
ENV GAME_MODE 1 
ENV MAP_GROUP mg_active 
ENV START_MAP de_dust2 

# Launching dedicated server 
WORKDIR /steamcmd/csgoserver 
CMD ./srcds_run \ 
  -game csgo \ 
  -console \ 
  -usercon \
  -tickrate 128 \
  +game_type $GAME_TYPE \ 
  +game_mode $GAME_MODE \ 
  +mapgroup $MAP_GROUP \ 
  +map $START_MAP 
