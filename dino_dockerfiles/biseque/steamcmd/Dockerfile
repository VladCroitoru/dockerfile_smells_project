FROM debian:latest
MAINTAINER biseque <info@biseque.com>

ENV STEAMCMD_PATH="/steamcmd"
ENV STEAMCMD="$STEAMCMD_PATH/steamcmd.sh"

RUN apt-get update
RUN apt-get install wget lib32gcc1 -y

WORKDIR $STEAMCMD_PATH

RUN wget https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz
RUN tar xf steamcmd_linux.tar.gz

CMD $STEAMCMD