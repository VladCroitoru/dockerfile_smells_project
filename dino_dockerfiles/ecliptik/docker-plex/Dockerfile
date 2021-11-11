FROM ubuntu:16.04
MAINTAINER Micheal Waltz <ecliptik@gmail.com>
#Thanks to https://github.com/bydavy/docker-plex/blob/master/Dockerfile,  https://github.com/aostanin/docker-plex/blob/master/Dockerfile, and https://github.com/timhaak/docker-plex

#Setup basic environment
ENV DEBIAN_FRONTEND=noninteractive \
    LANG=en_US.UTF-8 \
    LC_ALL=C.UTF-8 \
    LANGUAGE=en_US.UTF-8 \
    APPDIR=/app \
    PLEX_VERSION=1.4.3.3433-03e4cfa35

#Set Labels
LABEL org.label-schema.version="$PLEX_VERSION" \
      org.label-schema.vcs-url="https://github.com/ecliptik/docker-plex" \
      org.label-schema.vcs-ref="https://github.com/ecliptik/docker-plex/commits/master" \
      org.label-schema.vendor="Plex" \
      org.label-schema.name="docker-plex" \
      org.label-schema.docker.cmd="docker run -d --net="host" -h *your_host_name* -v /*your_config_location*:/config -v /*your_videos_location*:/data -p 32400:32400 plex"

#Set WORKDIR
WORKDIR ${APPDIR}

#Volumes
VOLUME /config
VOLUME /data

#Expose default Plex media port
EXPOSE 32400

#Install Plex
RUN set -ex && \
        buildDeps=' \
                curl \
                ca-certificates \
        ' && \
        apt-get update && \
        apt-get -y --allow-downgrades --allow-remove-essential --allow-change-held-packages upgrade && \
        apt-get install -y --no-install-recommends $buildDeps && \
        curl -O https://downloads.plex.tv/plex-media-server/${PLEX_VERSION}/plexmediaserver_${PLEX_VERSION}_amd64.deb && \
        dpkg --install --force-all plexmediaserver_*.deb && \
        apt-get purge -y --auto-remove $buildDeps && \
        apt-get clean && \
        rm -rf plexmediaserver_*.deb /var/lib/apt/lists/* /tmp/* /var/tmp/*

#Copy start script and make executable
COPY ./start.sh .
RUN chmod +x ./start.sh

#Set entrypoint of Plex start script
ENTRYPOINT [ "/app/start.sh" ]
