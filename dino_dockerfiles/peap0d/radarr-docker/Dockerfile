FROM mono

ARG RADARR_TAG="0.2.0.45"
ARG RADARR_FILENAME=Radarr.develop.v${RADARR_TAG}.linux
ARG RADARR_ZIP=Radarr.develop.${RADARR_TAG}.linux.tar.gz

RUN apt-get update \
  && apt-get install -y mediainfo wget \
  && rm -rf /var/lib/apt/lists/*


WORKDIR /opt
RUN wget "https://github.com/galli-leo/Radarr/releases/download/v$RADARR_TAG/$RADARR_ZIP"

RUN tar -xvzf /opt/$RADARR_ZIP

VOLUME /config

ENTRYPOINT ["mono", "/opt/Radarr/Radarr.exe", "-data=/config"]
