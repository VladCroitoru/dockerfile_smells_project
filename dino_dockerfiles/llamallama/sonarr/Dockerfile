FROM ubuntu:bionic
MAINTAINER Chris Jones <chris@sysadminchris.com> 

ENV UID=10001 UNAME=sonarr GID=10000 GNAME=media

RUN \
  groupadd -g $GID $GNAME && \
  useradd -M -u $UID -G $GNAME -s /usr/sbin/nologin $UNAME && \
  apt-get update && \
  apt-get -y install tzdata apt-transport-https gnupg libcurl3 && \
  apt-key adv --keyserver keyserver.ubuntu.com --recv-keys FDA5DFFC && \
  echo "deb https://apt.sonarr.tv/ master main" > /etc/apt/sources.list.d/sonarr.list && \
  apt-get update && \
  apt-get -y install \
    nzbdrone

RUN \
  mkdir -p /config /media && \
  chown $UNAME:$GNAME /config /media

EXPOSE 8989 

VOLUME /config
VOLUME /media

WORKDIR /opt/NzbDrone
USER $UNAME

ENTRYPOINT ["mono"]
CMD ["/opt/NzbDrone/NzbDrone.exe", "--nobrowser", "--data=/config"]

