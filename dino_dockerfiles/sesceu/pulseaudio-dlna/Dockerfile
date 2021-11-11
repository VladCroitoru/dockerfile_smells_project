FROM debian:sid
MAINTAINER Sebastian Schneider <mail@sesc.eu>

RUN apt-get update \
    && apt-get install -y pulseaudio-dlna \
    && rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["pulseaudio-dlna"]
