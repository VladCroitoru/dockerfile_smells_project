FROM debian:jessie

MAINTAINER Daniel Holz <dgholz@gmail.com>

RUN apt-get update --quiet=2 && \
      DEBIAN_FRONTEND=noninteractive apt-get install --quiet=2 python git
RUN DEBIAN_FRONTEND=noninteractive apt-get install --quiet=2 shntool libav-tools

RUN mkdir -p /headphones/config
RUN /bin/bash -c "mkdir -p /headphones/{torrent,usenet}/{blackhole,download}"
RUN mkdir -p /headphones/music

EXPOSE 8181

RUN git clone https://github.com/rembo10/headphones /opt/headphones

CMD [ "--datadir", "/headphones/config", "--nolaunch" ]
ENTRYPOINT [ "/opt/headphones/Headphones.py" ]
