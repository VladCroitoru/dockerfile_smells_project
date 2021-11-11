FROM yuiofthesun/openjdk8jre

MAINTAINER yuiofthesun


RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -yq wget


RUN wget -P /home/regrowthkat/ http://ftb.cursecdn.com/FTB2/modpacks/Regrowth/0_9_1/RegrowthServer.zip

RUN DEBIAN_FRONTEND=noninteractive apt-get install -yq unzip

RUN  unzip /home/regrowthkat/RegrowthServer.zip -d /home/regrowthkat/ && rm /home/regrowthkat/RegrowthServer.zip

RUN echo "#By changing the setting below to TRUE you are indicating your agreement to our EULA (https://account.mojang.com/documents/minecraft_eula)\n. #Mon Mar 07 13:36:02 CET 2016 \n eula=true" >> /home/regrowthkat/eula.txt


COPY regrowthwrapper.sh /home/regrowthkat/

RUN chmod 744 /home/regrowthkat/regrowthwrapper.sh

CMD ./regrowthwrapper.sh

EXPOSE 25565:25565
VOLUME /home/regrowthkat/world
WORKDIR /home/regrowthkat   




