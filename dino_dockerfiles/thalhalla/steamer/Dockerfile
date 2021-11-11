FROM ubuntu:xenial
MAINTAINER Josh Cox <josh 'at' webhosting coop>

ENV LANG=en_US.UTF-8 \
  LANGUAGE=en_US.UTF-8 \
  STEAM_USERNAME=anonymous \
  STEAM_PASSWORD=' ' \
  DEBIAN_FRONTEND=noninteractive \
  STEAMER_UPDATED=20181209 \
  STEAM_FORCE_INSTALL=/data
#ENV LC_ALL en_US.UTF-8
#APT
COPY sources.list /etc/apt/sources.list.d/thalhalla.list

RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys F24AEA9FB05498B7 && \
dpkg --add-architecture i386 && \
apt-get -yqq update && \
apt-get install -yqq locales && \
dpkg-reconfigure --frontend=noninteractive locales && \
sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
locale-gen && \
apt-get install -yqq sudo wget lib32stdc++6 lib32z1 lib32z1-dev net-tools procps \
libcurl4-gnutls-dev:i386 build-essential gdb mailutils postfix curl wget file \
lib32ncurses5 libasound2 fail2ban unzip gettext-base \
gzip bzip2 bsdmainutils python util-linux \
tmux byobu lib32gcc1 libstdc++6 libstdc++6:i386 && \
rm -rf /var/lib/apt/lists/*

# End non-interactive apt
ENV DEBIAN_FRONTEND interactive

# parking lot
# echo "steam steam/purge note" |  debconf-set-selections && \
# echo "steam steam/license note" |  debconf-set-selections && \
# echo "steam steam/question select I AGREE" |  debconf-set-selections && \
# apt-get install -yqq steam steamcmd && \

# and override this file with the command to start your server
COPY assets /assets
RUN \
chmod 755 /assets/steamer.txt && \
useradd -m -s /bin/bash steamer && \
usermod -a -G sudo,video,audio,tty steamer && \
echo '%sudo ALL=(ALL) NOPASSWD:ALL'>> /etc/sudoers && \
chown -R steamer. /home/steamer && \
mkdir -p /opt/steamer && \
chown -R steamer. /opt/steamer && \
mkdir -p /data && \
chown -R steamer. /data && \
locale-gen

USER steamer
WORKDIR /opt/steamer/
RUN curl -sqL 'https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz' | tar zxf -

WORKDIR /data

VOLUME /home/steamer
VOLUME /data
CMD ["/assets/steamer"]
