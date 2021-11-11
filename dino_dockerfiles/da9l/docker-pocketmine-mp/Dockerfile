FROM ubuntu:14.04.2

MAINTAINER da9l https://github.com/da9l

RUN apt-get update -y && \
        apt-get install -y \
        autoconf \
        automake \
        g++ \
        gcc \
        gcc-multilib \
        libtool \
        m4 \
        make \
        perl \
        wget

RUN adduser --gecos 'PocketMine-MP' --disabled-password --home /pocketmine pocketmine

WORKDIR /pocketmine
RUN mkdir /pocketmine/PocketMine-MP
RUN mkdir /pocketmine/PocketMine-MP/plugins
RUN chown -R pocketmine:pocketmine /pocketmine

COPY assets/server.properties /pocketmine/server.properties.original
COPY assets/entrypoint.sh /pocketmine/entrypoint.sh
#COPY assets/plugins.sh /pocketmine/plugins.sh

#RUN chmod 755 /pocketmine/plugins.sh
RUN chmod 755 /pocketmine/entrypoint.sh

USER pocketmine

ENV GNUPGHOME /pocketmine

RUN gpg --keyserver pgp.mit.edu --recv-key 2280B75B
RUN cd PocketMine-MP && wget -q -O - http://cdn.pocketmine.net/installer.sh | bash -s - -v beta

RUN wget -q -O /pocketmine/PocketMine-MP/plugins/EssentialsPE.phar https://forums.pocketmine.net/plugins/essentialspe.886/download?version=1722  
RUN wget -q -O /pocketmine/PocketMine-MP/plugins/chatbubbles.phar https://forums.pocketmine.net/plugins/chatbubbles.671/download?version=1409
RUN wget -q -O /pocketmine/PocketMine-MP/plugins/manyworlds.phar https://forums.pocketmine.net/plugins/manyworlds.1042/download?version=2145
RUN wget -q -O /pocketmine/PocketMine-MP/plugins/worldgm.phar https://forums.pocketmine.net/plugins/worldgm.844/download?version=2073
RUN wget -q -O /pocketmine/PocketMine-MP/plugins/volt.phar https://forums.pocketmine.net/plugins/volt.568/download?version=1999
RUN wget -q -O /pocketmine/PocketMine-MP/plugins/commandsigns.phar https://forums.pocketmine.net/plugins/commandsigns.958/download?version=1856
#RUN wget -q -O /pocketmine/PocketMine-MP/plugins/autoupdater.phar https://forums.pocketmine.net/plugins/autoupdater.854/download?version=1700


#RUN /pocketmine/plugins.sh

EXPOSE 19132
EXPOSE 19132/udp
EXPOSE 7000

ENTRYPOINT ["./entrypoint.sh"]
