FROM debian:8

RUN apt-get update -q && \
  apt-get install -qy \
  lib32gcc1 curl && \
  apt-get clean

RUN useradd -m steam
USER steam
WORKDIR /home/steam

RUN curl -sqL "https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz" \
    | tar zxvf -

ENTRYPOINT ["/home/steam/steamcmd.sh"]
