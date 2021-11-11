FROM debian:jessie
MAINTAINER verti vertical0520@gmail.com
ADD entrypoint.sh /entrypoint.sh
RUN chmod 755 /entrypoint.sh && \
    apt-get -q update && \
    apt-get -q install -y \
    x11vnc \
    xinit \
    xvfb \
    unzip \
    libxcursor1 \
    bzip2 \
    screen \
    wget \
    unzip \
    ca-certificates \
    libglib2.0-0 \
    youtube-dl && \
    mkdir /opt/ts3soundboard/ && \
    cd /opt/ts3soundboard/ && \
    wget vertipl.me/sinusv2yt.zip && \
    unzip sinusv2yt.zip 

VOLUME ["/sinus"]
EXPOSE 8087
ENTRYPOINT ["/entrypoint.sh"]
