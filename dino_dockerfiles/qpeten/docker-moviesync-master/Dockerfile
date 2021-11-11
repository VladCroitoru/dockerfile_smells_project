# Created by Quentin Peten on the 17th of August 2017
# This container is supposed to create and seed a torrent file per folder (=movie)

FROM ubuntu:16.04

ENV UID 1000
ENV GID 1000

RUN apt-get update && apt-get install -y transmission transmission-cli transmission-daemon transmission-remote-cli lua5.3

RUN groupadd -g $GID user && useradd --no-create-home -g user --uid $UID user

WORKDIR /torrents

COPY ./launch.bash /launch.bash
COPY ./movieSync.lua /movieSync.lua
RUN chmod 755 /launch.bash /movieSync.lua && chown user /launch.bash /movieSync.lua

VOLUME  /transmission-config /movies /torrents

USER user

CMD ["/launch.bash"]
