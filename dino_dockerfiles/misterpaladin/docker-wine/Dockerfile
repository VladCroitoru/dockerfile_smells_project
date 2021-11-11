FROM x11docker/xfce:latest
MAINTAINER Eugene Min <e.min@milax.com>

RUN apt-get update

RUN echo "deb http://ppa.launchpad.net/ubuntu-wine/ppa/ubuntu xenial main"        > /etc/apt/sources.list.d/wine_ppa.list
RUN apt-key adv --recv-keys --keyserver keyserver.ubuntu.com     883E8688397576B6C509DF495A9A06AEF9CB8DB0

RUN dpkg --add-architecture i386
RUN apt-get update

RUN apt-get install -y wine1.8
RUN apt-get install -y winetricks

RUN apt-get update -y
RUN apt-get install -y \
    sudo \
    nano \
    wget \
    curl \
    openssh-client \
    git \
    wine

RUN wget https://nodejs.org/download/release/v4.4.4/node-v4.4.4-linux-x64.tar.gz
RUN tar -C /usr/local --strip-components 1 -xzf node-v4.4.4-linux-x64.tar.gz
RUN npm -g install npm
RUN npm -g install gulp
RUN npm -g install electron
RUN npm -g install electron-packager
