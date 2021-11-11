FROM ubuntu
MAINTAINER Cameron Boulton <https://github.com/iAnomaly>

RUN useradd -m steam
RUN apt-get update && apt-get install -y --no-install-recommends \
lib32gcc1 \
#ca-certificates \
wget
RUN apt-get upgrade -y
RUN mkdir /mnt/steam
RUN chown steam:steam /mnt/steam
USER steam
RUN mkdir ~/steamcmd
WORKDIR /home/steam/steamcmd
RUN wget http://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz
RUN tar -xvzf steamcmd_linux.tar.gz \
&& rm steamcmd_linux.tar.gz
RUN ./steamcmd.sh +quit 
USER root

