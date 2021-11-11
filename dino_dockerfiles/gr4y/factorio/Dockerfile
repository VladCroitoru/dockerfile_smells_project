# Factorio
# docker run -d -p 34197:34197/udp -v /data/factorio/saves:/opt/factorio/saves -v /data/factorio/mods:/opt/factorio/mods --name factorio gr4y/factorio

FROM ubuntu:xenial

MAINTAINER Sascha Wessel <swessel@gr4yweb.de>

# Update System
RUN apt-get -y update && apt-get -y upgrade && apt-get install -y wget && rm -rf /var/lib/apt/lists/*

# Download Factorio Server
RUN mkdir /opt/factorio && cd /opt/factorio
RUN wget -c https://www.factorio.com/get-download/0.16.51/headless/linux64 -O - | tar -xf -C /opt/

# Install init.sh
ADD run.sh /opt/factorio/

WORKDIR /opt/factorio
VOLUME ["/opt/factorio/saves", "/opt/factorio/mods"]

EXPOSE 34197/udp

# Run minecraft.service
CMD ["/opt/factorio/run.sh"]
