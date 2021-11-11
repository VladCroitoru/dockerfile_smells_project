# Plex
#
# Version: 0.0.10

FROM fedora:24
MAINTAINER Nicholas Moore

VOLUME /var/lib/plexmediaserver/
VOLUME /media

ADD ./start.sh /start.sh

RUN cp /usr/share/zoneinfo/US/Pacific /etc/localtime;\
    rpm -ivh --force https://downloads.plex.tv/plex-media-server/1.0.0.2261-a17e99e/plexmediaserver-1.0.0.2261-a17e99e.x86_64.rpm
EXPOSE 32400

ENTRYPOINT ["/start.sh"]
