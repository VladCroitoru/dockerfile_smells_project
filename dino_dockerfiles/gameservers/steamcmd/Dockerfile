FROM ubuntu:18.04

MAINTAINER Jason Rivers <docker@jasonrivers.co.uk

ENV DEBIAN_FRONTEND noninteractive
ENV STEAM_USER anonymous

# Install dependencies
RUN dpkg --add-architecture i386
RUN apt-get update                      &&      \
    apt-get upgrade -y                     &&      \
    apt-get install -y                          \
        curl                                    \
        lib32gcc1				\
	lib32tinfo5				\
	libncurses5				\
	libncurses5:i386			\
	libc6:i386				\
	libstdc++6:i386				\
	lib32z1					\
	libcurl3-gnutls:i386
					

RUN useradd                             \
        -d /home/steamsrv               \
        -m                              \
        -s /bin/bash                    \
        steamsrv

RUN mkdir -p /scripts
ADD InstallAppID /scripts/InstallAppID
ADD run_srcds_server /scripts/run_srcds_server
ADD StartServer /scripts/StartServer

USER steamsrv
# Download and extract SteamCMD
RUN mkdir -p /home/steamsrv/steamcmd            &&\
    cd /home/steamsrv/steamcmd                          &&\
    curl -s http://media.steampowered.com/installer/steamcmd_linux.tar.gz | tar -vxz &&\
    mkdir -p /home/steamsrv/.steam/sdk32		&&\
    ln -s /home/steamsrv/steamcmd/linux32/steamclient.so /home/steamsrv/.steam/sdk32/steamclient.so
	

WORKDIR /home/steamsrv

RUN /home/steamsrv/steamcmd/steamcmd.sh +login anonymous +quit

