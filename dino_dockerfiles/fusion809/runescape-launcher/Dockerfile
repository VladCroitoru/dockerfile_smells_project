# Maintainer: Brenton Horne <brentonhorne77 at gmail dot com>
# Contributor: Mordeth http://services.runescape.com/m=forum/c=BayWIRvWZa8/users.ws?searchname=Mordeth&lookup=view
FROM ubuntu:14.04

RUN apt-get update && apt-get install -y \
    apt-transport-https \
    wget \
    libcurl3 \
    libcurl4-openssl-dev \
    xserver-xorg-video-intel \
    packagekit-gtk3-module \
    libcanberra-gtk-module \
    alsa-utils \
    libasound2-plugins \
    libcanberra-pulse \
    gvfs \
    libpcre3
        
RUN wget -O - https://content.runescape.com/downloads/ubuntu/runescape.gpg.key | apt-key add - && \
    mkdir -p /etc/apt/sources.list.d && \
    echo "deb https://content.runescape.com/downloads/ubuntu trusty non-free" > /etc/apt/sources.list.d/runescape.list && \
    apt-get update && \
    apt-get install -y runescape-launcher

ENV HOME /home/runescape
RUN useradd --create-home --home-dir $HOME runescape \
    && gpasswd -a runescape audio \
    && chown -R runescape:runescape $HOME
WORKDIR $HOME
USER runescape

CMD /usr/bin/runescape-launcher
