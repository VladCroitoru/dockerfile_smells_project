FROM ubuntu:15.04
MAINTAINER Mark McGuire "mark.b.mcg@gmail.com"

RUN dpkg --add-architecture i386 \
    && apt-get -y update \
    && apt-get -y install lib32gcc1 lib32stdc++6 wget \
    && wget -q http://media.steampowered.com/installer/steamcmd_linux.tar.gz -O /tmp/steamcmd_linux.tar.gz \
    && mkdir /opt/steam \
    && cd /opt/steam \
    && tar -xzf /tmp/steamcmd_linux.tar.gz \
    && /opt/steam/steamcmd.sh +quit \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
