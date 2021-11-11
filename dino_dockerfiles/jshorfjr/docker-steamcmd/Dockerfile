# SteamCMD Dockerfile for Ubuntu 14.04 Trusty
# Step by step documentation found on Valve Developer Wiki
# https://developer.valvesoftware.com/wiki/SteamCMD#Linux

FROM ubuntu:14.04

MAINTAINER Jeffrey Shorf Jr. <jsho4realyo@gmail.com>

# Install dependencies required to run SteamCMD
RUN apt-get update &&\
    apt-get install curl lib32gcc1 -y

# Create directory, switch to it, download SteamCMD for Linux, Extract
RUN mkdir -p /opt/steamcmd &&\
    cd /opt/steamcmd &&\
    curl -s http://media.steampowered.com/installer/steamcmd_linux.tar.gz | tar xvz

WORKDIR /opt/steamcmd

ENTRYPOINT ["./steamcmd.sh"]
