FROM ubuntu:latest
MAINTAINER Robert Soeting <robert@soeting.net>

RUN apt-get -y install python3-yaml curl

RUN mkdir /pocketmine
RUN cd /pocketmine && curl -sL http://get.pocketmine.net/ | bash -s - -r -v stable

VOLUME /pocketmine
WORKDIR /pocketmine

EXPOSE 19132

CMD ["./start.sh", "--no-wizard", "--enable-rcon=on"]
