FROM ubuntu:latest

MAINTAINER Marcelo Bartsch <mbartsch@bartsch.cl>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -qq -y update && \
    apt-get -qq -y install icecast2 mpc mpd && \
    apt-get clean
RUN mkdir -p /opt/music && \
    mkdir -p /opt/playlists && \
    chown mpd. /opt/music /opt/playlists

CMD ["/start.sh"]
EXPOSE 8000 6600
VOLUME ["/config", "/var/log/icecast2", "/etc/icecast2","/opt/music","/opt/playlists"]

ADD ./mpd.conf /etc/mpd.conf
ADD ./start.sh /start.sh
ADD ./icecast.xml /etc/icecast/icecast.xml
ADD ./icecast2 /etc/default/icecast2
RUN chown -R icecast2 /etc/icecast2
RUN echo 'mpd : ALL' >> /etc/hosts.allow
