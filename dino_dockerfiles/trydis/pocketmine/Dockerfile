FROM centos

MAINTAINER Morten Trydal <trydis@hotmail.com>

RUN yum install -y \
    git libtool-ltdl \
    && yum clean all \
    && groupadd -r pocketmine && useradd -r -g pocketmine pocketmine \
    && mkdir /pocketmine \
    && chown -R pocketmine:pocketmine /pocketmine \
    && git clone --recursive -b 1.6.2dev-3.0.0-ALPHA4 https://github.com/pmmp/pocketmine-mp.git pocketmine \
    && curl -LO https://bintray.com/pocketmine/PocketMine/download_file?file_path=PHP_7.0.6_x86-64_Linux.tar.gz \
    && tar -xvzf download_file\?file_path\=PHP_7.0.6_x86-64_Linux.tar.gz -C /pocketmine \
    && rm -f download_file\?file_path\=PHP_7.0.6_x86-64_Linux.tar.gz

WORKDIR /pocketmine
USER pocketmine

RUN echo $'server-name=Minecraft: PE Server\n\
server-port=19132\n\
gamemode=1\n\
max-players=20\n\
spawn-protection=16\n\
white-list=off\n\
enable-query=on\n\
enable-rcon=off\n\
rcon.password=\n\
motd=Minecraft: PE Server\n\
announce-player-achievements=on\n\
allow-flight=off\n\
spawn-animals=on\n\
spawn-mobs=on\n\
force-gamemode=off\n\
hardcore=off\n\
pvp=on\n\
difficulty=1\n\
generator-settings=\n\
level-name=world\n\
level-seed=\n\
level-type=DEFAULT\n\
auto-save=on'> ./server.properties

EXPOSE 19132

CMD ["./start.sh"]