FROM debian
MAINTAINER Iskaron <mail@iskaron.de>

RUN apt-get update && apt-get install -y wget bzip2 locales && rm -rf /var/lib/apt/lists/*
ENV TS_DIR /opt/teamspeak3-server_linux_amd64

RUN locale-gen de_DE.UTF-8
ENV LANG de_DE.UTF-8
ENV LANGUAGE de_DE:de
ENV LC_ALL de_DE.UTF-8

RUN mkdir -p $TS_DIR
RUN useradd -s /bin/bash teamspeak
RUN chown teamspeak $TS_DIR -R

RUN locale-gen de_DE.UTF-8  
ENV LANG de_DE.UTF-8  
ENV LANGUAGE de_DE:en  
ENV LC_ALL de_DE.UTF-8  

RUN ln -s /opt/teamspeak3-server_linux_amd64 /opt/ts3

ENV TS_VERSION 3.13.5
RUN wget -O - https://files.teamspeak-services.com/releases/server/$TS_VERSION/teamspeak3-server_linux_amd64-$TS_VERSION.tar.bz2 | tar xvfj - -C /opt


