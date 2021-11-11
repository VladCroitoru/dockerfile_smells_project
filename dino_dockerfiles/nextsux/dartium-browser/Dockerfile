FROM debian:latest
MAINTAINER Martin -nexus- Mlynář <nexus+docker@smoula.net>

COPY files/run.sh /run.sh

ENV VERSION=1.25.0-dev.6.0
ENV VERSION_DIR_EXT=.0
ENV DISPLAY=:0
ENV UID=1000
ENV GID=1000

VOLUME ["/tmp/.X11-unix", "/home/user/"]

RUN apt-get update && apt-get install -y chromium wget unzip libgconf-2-4 libexif12 xterm
WORKDIR /opt/
RUN wget https://storage.googleapis.com/dart-archive/channels/dev/release/$VERSION/dartium/dartium-linux-x64-release.zip -O dartium.zip
RUN unzip ./dartium.zip && mv /opt/dartium-linux-x64-dev-$VERSION$VERSION_DIR_EXT /opt/dartium

RUN useradd -m user -u 1000

CMD ["/run.sh"]
