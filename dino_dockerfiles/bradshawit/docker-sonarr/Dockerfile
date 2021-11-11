FROM ubuntu:xenial

RUN apt-get update -q && \
    apt-get upgrade -qy && \
    apt-get install -qy libcurl4-openssl-dev && \
    apt-get install -qy mono-devel && \
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys FDA5DFFC && \
    echo "deb http://apt.sonarr.tv/ master main" | tee /etc/apt/sources.list.d/sonarr.list && \
    apt-get update -q && \
    apt-get install -qy nzbdrone && \
    apt-get clean
    
ADD launch.sh /launch.sh
RUN chmod +x "/launch.sh"

EXPOSE 8989

VOLUME  ["/data/downloads"]
VOLUME  ["/data/torrentfiles"]
VOLUME  ["/data/tv"]
VOLUME  ["/data/sonarr"]

# CMD ["mono --debug /opt/NzbDrone/NzbDrone.exe"]
CMD ["/launch.sh"]
