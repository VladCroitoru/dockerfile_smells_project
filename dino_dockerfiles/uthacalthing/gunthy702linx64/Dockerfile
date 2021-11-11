FROM debian:latest

# update and upgrade
RUN apt-get -y update && \
  apt-get -y upgrade

# install requirements
RUN apt-get -y install wget
RUN apt-get -y install unzip
RUN apt-get -y install gosu

# cleanup
RUN apt-get clean -y && \
  apt-get autoclean -y && \
  apt-get autoremove -y && \
  rm -rf /usr/share/locale/* && \
  rm -rf /var/cache/debconf/*-old && \
  rm -rf /var/lib/apt/lists/* && \
  rm -rf /usr/share/doc/*

# create a gunbot and gunbot-data folder to hold files
RUN mkdir /gunbot;

# go in that folder
WORKDIR /gunbot

# get gunthy
RUN wget https://github.com/GuntharDeNiro/BTCT/releases/download/702/Gunbot.XT.Edition.-.Linux.package.zip

# uncompress gunthy files in /gunbot
RUN unzip Gunbot.XT.Edition.-.Linux.package.zip && \
  rm -f Gunbot.XT.Edition.-.Linux.package.zip && \
  mv "Gunbot XT Edition - Linux package" gunthy-files && \
  mv gunthy-files/* . && \
  rmdir gunthy-files && \
  chmod +x gunthy-*;

# create a default /gunbot-data
# This folder is intented to contains
# - config.js: the current configuration loaded in gunbot
# - db.sqlite: the current configuration and data from gunthy-gui
# - err.log: the gunbot error stream
# - out.log: the gunbot output stream
# To keep thos files outside of container, mount a volumne on /gunbot-data on run
RUN mkdir /gunbot-data

LABEL description="Gunbot data files are stored in /gunbot-data \
You should mount a volume on that directory if you want to access files from the host"

# make symlinks in /gunbot to point to /gunbot-data files
#RUN mv /gunbot/config.js /gunbot-data/config.js && \
#  touch /gunbot-data/db.sqlite && \
#  touch /gunbot-data/err.log && \
#  touch /gunbot-data/out.log && \
RUN mv config.js config.js.origin && \
  ln -s /gunbot-data/config.js config.js && \
  ln -s /gunbot-data/db.sqlite db.sqlite && \
  ln -s /gunbot-data/err.log err.log && \
  ln -s /gunbot-data/out.log out.log;

# Expose port 5000 for access to gunthy-gui
EXPOSE 5000

# add init script inside
ADD ./run.sh /gunbot/run.sh
RUN chmod +x /gunbot/run.sh

# launch init script and gunthy
ENTRYPOINT ["/gunbot/run.sh"]

