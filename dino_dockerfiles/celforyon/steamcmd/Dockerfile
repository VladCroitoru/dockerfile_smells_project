FROM debian:latest

LABEL maintainer="Alexis Pereda <alexis@pereda.fr>"
LABEL version="1.0"
LABEL description="steamcmd"

ENV STEAMCMD_URL "http://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz"

RUN dpkg --add-architecture i386
RUN apt update \
	&& apt install --no-install-recommends --no-install-suggests -y \
		lib32gcc1 lib32stdc++6 libcurl4-gnutls-dev:i386 wget sudo \
	&& rm -rf /var/lib/apt/lists/*

RUN useradd -ms /bin/bash steam
USER steam
WORKDIR /home/steam

RUN mkdir bin apps

WORKDIR /home/steam/bin
RUN wget -cO steamcmd_linux.tar.gz $STEAMCMD_URL
RUN tar zxf steamcmd_linux.tar.gz&&rm steamcmd_linux.tar.gz
RUN ln -s $(pwd)/steamcmd.sh $(pwd)/steamcmd

WORKDIR /home/steam
RUN bin/steamcmd +quit
