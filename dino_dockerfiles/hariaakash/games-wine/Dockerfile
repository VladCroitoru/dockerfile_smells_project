# ----------------------------------
# Pterodactyl Core Dockerfile
# Environment: FOR WINDOWS GAMES
# ----------------------------------
FROM 		ubuntu:16.04

MAINTAINER 	Hari Narayanan, <smgdark@gmail.com>

ENV         DEBIAN_FRONTEND noninteractive

RUN 		dpkg --add-architecture i386 \
			&& apt-get update \
			&& apt-get upgrade -y \
			&& apt-get install -y unzip curl \
			&& useradd -m -d /home/container container

#RUN 		apt-get install -y software-properties-common && add-apt-repository -y ppa:ubuntu-wine/ppa \
#			&& apt-get update -y
			
RUN			apt-get install -y wine winetricks \
			&& apt-get purge -y software-properties-common \
			&& apt-get autoclean -y
				
USER container
ENV  HOME /home/container
WORKDIR /home/container

COPY 	./entrypoint.sh /entrypoint.sh

CMD 	["/bin/bash", "/entrypoint.sh"]