FROM ubuntu:xenial

RUN apt-get update && apt-get install -y lib32gcc1 ssh telnet curl

RUN useradd --uid 1001 steam && mkdir /home/steam && chown steam:steam /home/steam

VOLUME /home/steam

USER steam

CMD /home/steam/start.sh
