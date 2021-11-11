FROM openjdk:8-jdk
MAINTAINER f.fernandes@fernandes-it.de

ADD https://www.feed-the-beast.com/projects/ftb-presents-hermitpack/files/2369307/download /root/hermitpack.zip

RUN unzip /root/hermitpack.zip -d /hermitpack && \
    rm /root/hermitpack.zip && \
    chmod +x /hermitpack/*.sh && \
    echo "eula=true" > /hermitpack/eula.txt && \
    mkdir /hermitpack/mc-config/ && \
    echo "[]" > /hermitpack/mc-config/ops.json && \
    echo "[]" > /hermitpack/mc-config/whitelist.json && \
    echo "[]" > /hermitpack/mc-config/banned-ips.json && \
    echo "[]" > /hermitpack/mc-config/banned-players.json && \
    ln -s /hermitpack/mc-config/ops.json /hermitpack/ops.json && \
    ln -s /hermitpack/mc-config/whitelist.json /hermitpack/whitelist.json && \
    ln -s /hermitpack/mc-config/banned-ips.json /hermitpack/banned-ips.json && \
    ln -s /hermitpack/mc-config/banned-players.json /hermitpack/banned-players.json && \
    apt-get update && \
    apt-get install -y --no-install-recommends tmux && \
    rm -rf /var/lib/apt/lists/*



VOLUME /hermitpack/world
VOLUME /hermitpack/backups
VOLUME /hermitpack/mc-config

EXPOSE 25565

CMD ["tmux", "new-session", "-s", "minecraft", "/bin/bash -l -c /hermitpack/ServerStart.sh" ]
