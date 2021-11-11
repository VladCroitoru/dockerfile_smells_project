FROM node:slim

MAINTAINER Zeyu Ye <Shuliyey@gmail.com>

RUN apt-get update \
  && apt-get install -y git unzip \
  && yarn global add ionic cordova \
  && apt-get clean -y \
  && apt-get autoclean -y \
  && apt-get autoremove -y \
  && rm -rf /usr/share/locale/* \
  && rm -rf /var/cache/debconf/*-old \
  && rm -rf /var/lib/apt/lists/* \
  && rm -rf /usr/share/doc/*

CMD ["bash"]
