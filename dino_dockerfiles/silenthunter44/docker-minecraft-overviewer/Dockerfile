FROM debian:stretch-slim

LABEL maintainer="guillaume.connan44@gmail.com"
LABEL version="0.2.0"

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
    apt-get install -y wget gnupg && \
    echo "deb http://overviewer.org/debian ./" >> /etc/apt/sources.list && \
    wget -O - https://overviewer.org/debian/overviewer.gpg.asc | apt-key add - && \
    apt-get update && \
    apt-get dist-upgrade -y && \
    apt-get install -y minecraft-overviewer && \
    mkdir -p /in /temp /out && \
    useradd -m minecraft && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY entrypoint.sh /home/minecraft/entrypoint.sh
COPY download_url.py /home/minecraft/download_url.py

RUN chown minecraft:minecraft -R /home/minecraft/ /temp/

VOLUME /in /out

WORKDIR /home/minecraft/

USER minecraft

CMD bash /home/minecraft/entrypoint.sh
