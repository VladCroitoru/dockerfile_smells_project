#
# Base image
#

FROM debian:latest
MAINTAINER elfalem <elfalem@gmail.com>

RUN apt-get update
RUN apt-get install -y python python-pip vim sudo

ENV BEETSDIR /config
ENV EDITOR vim

RUN useradd -m beets

#allow sudo
RUN echo beets:beets | chpasswd
RUN usermod -a -G sudo beets

#volumes
RUN mkdir /config
RUN mkdir /downloads
RUN ln -s /home/beets/Music /music

#install beets dependencies
RUN pip install jellyfish mutagen munkres unidecode pyyaml musicbrainzngs
