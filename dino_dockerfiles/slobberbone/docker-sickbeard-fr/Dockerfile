FROM ubuntu:14.04

#ENV SICKBEARD_VERSION torrent_1080_subtitles
#ENV SICKBEARD_VERSION build-506

RUN apt-get -q update &&\
    apt-get -qy --force-yes dist-upgrade

RUN apt-get install -qy --force-yes python-cheetah python-setuptools wget tar ca-certificates curl git

RUN git clone https://gitlab.com/sarakha63/Sick-Beard.git /sickbeard

# apt clean
RUN apt-get clean &&\
  rm -rf /var/lib/apt/lists/* &&\
  rm -rf /tmp/*

# map /config to host defined config path (used to store configuration from app)
VOLUME /config
# map /data to host defined data path (used to store downloads or use blackhole)
VOLUME /data
# map /media to host defined media path (used to read/write to media library)
VOLUME /media

ADD ./start.sh /start.sh
RUN chmod u+x  /start.sh

EXPOSE 8081

CMD ["/start.sh"]
