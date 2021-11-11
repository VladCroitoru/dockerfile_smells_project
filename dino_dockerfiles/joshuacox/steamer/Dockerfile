FROM debian:jessie
MAINTAINER Josh Cox <josh 'at' webhosting coop>

#APT
RUN echo 'deb http://http.debian.net/debian/ jessie main contrib non-free'>>/etc/apt/sources.list ; \
dpkg --add-architecture i386 ; \
apt-get -y update ; \
apt-get install -y sudo wget lib32stdc++6 lib32z1 lib32z1-dev net-tools ; \
bsdmainutils tmux mailutils postfix ca-certificates lib32gcc1 libstdc++6:i386 ; \
rm -rf /var/lib/apt/lists/*

ENV STEAMER_UPDATED 20160715

# override these variables in with the prompts
ENV STEAM_USERNAME anonymous
ENV STEAM_PASSWORD ' '


# and override this file with the command to start your server
COPY assets /assets
RUN chmod 755 /assets/start.sh ; \
chmod 755 /assets/run.sh ; \
chmod 755 /assets/steamer.txt ; \
chmod 755 /assets/steamcmdinstaller3.9.sh ; \
useradd -m -s /bin/bash steam ; \
usermod -a -G sudo,video,audio steam ; \
echo '%sudo ALL=(ALL) NOPASSWD:ALL'>> /etc/sudoers ; \
chown -R steam. /home/steam

USER steam
WORKDIR /home/steam/


#USER root
#ENTRYPOINT ["/bin/bash"]
CMD ["/bin/bash",  "/assets/start.sh"]
