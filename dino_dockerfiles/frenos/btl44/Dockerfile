FROM ubuntu:latest
MAINTAINER Frenos <Frederic@codepotion.de>
ARG DEBIAN_FRONTEND="noninteractive"

ENV SERVER_PORT=7777

#Serverconfiguration default values
ENV SERVERNAME="Community Server frenos/btl44"
ENV PASSWORD=
ENV PLAYMODE=Arcade
ENV ADMINSTEAMID=000000000000000
ENV STARTTYPE=ReadyUp
ENV REQUIREDPLAYERS=2

RUN apt-get update && apt-get install -y wget unzip lib32gcc1 xdg-user-dirs curl

RUN mkdir /steam && curl http://media.steampowered.com/client/steamcmd_linux.tar.gz | tar -C /steam -xvz

ADD scmd_script.txt /steam

WORKDIR /LinuxServer/Linux/

ADD myrunner.sh .
RUN chmod +x ./myrunner.sh

EXPOSE ${SERVER_PORT}

CMD ./myrunner.sh
