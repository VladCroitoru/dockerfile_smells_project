FROM fedora:latest

RUN dnf install -y glibc-minimal-langpack.x86_64 && dnf clean all

RUN dnf install -y https://downloads.plex.tv/plex-media-server/1.4.3.3433-03e4cfa35/plexmediaserver-1.4.3.3433-03e4cfa35.x86_64.rpm && dnf clean all

VOLUME /media
VOLUME /config

EXPOSE 32400/tcp

ADD run.sh /

CMD ["/run.sh"]
