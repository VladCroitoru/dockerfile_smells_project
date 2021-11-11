#version 1.2
FROM debian:jessie

WORKDIR /home

RUN apt-get update && apt-get install -y wget libc6-i386 vlc vlc-data vlc-plugin-pulse browser-plugin-vlc mplayer2 && apt-get purge && rm -rf /var/lib/apt/lists/* && apt-get clean
RUN wget -O- http://simple-help.com/releases/SimpleHelp-linux-amd64.tar.gz | tar -xzv 

WORKDIR /home/SimpleHelp

RUN sed -i 's/&//g' serverstart.sh


CMD ["sh", "serverstart.sh"]
