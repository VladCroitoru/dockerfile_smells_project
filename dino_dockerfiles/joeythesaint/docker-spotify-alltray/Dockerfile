FROM ubuntu:16.04
MAINTAINER Joe MacDonald <joe@deserted.net>

# Install Spotify and PulseAudio.
WORKDIR /usr/src
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 0DF731E45CE24F27EEEB1450EFDC8610341D9410 \
	&& echo deb http://repository.spotify.com stable non-free > /etc/apt/sources.list.d/spotify.list \
	&& apt-get update \
	&& apt-get install -y \
		   spotify-client xdg-utils libxss1 \
		   pulseaudio \
		   fonts-noto \
		   libwnck22 \
	&& apt-get clean \
	&& echo enable-shm=no >> /etc/pulse/client.conf

# Alltray will put Spotify into our system tray, but unfortunately the upstream
# one is unmaintained and no longer works properly with the sytem tray, so
# we'll bring in an old one that needs its own libgtop but at least docks
# properly.
COPY alltray /usr/bin/
COPY libgtop-2.0.so.7.2.0 /usr/lib/
RUN cd /usr/lib \
	&& ln -s libgtop-2.0.so.7.2.0 libgtop-2.0.so.7 \
	&& ln -s libgtop-2.0.so.7 libgtop-2.0.so

ENV USER_UID=${USER_UID:-1000}
ENV USER_GID=${USER_GID:-1000}
RUN groupadd -f -g ${USER_GID} spotify \
	&& adduser --uid ${USER_UID} --gid ${USER_GID} \
		   --disabled-password --gecos 'Spotify' spotify

ENV DISPLAY=unix${DISPLAY:-:0.0}

# Spotify data.
VOLUME ["/data/cache", "/data/config"]
RUN mkdir -p /data/cache \
	&& mkdir -p /data/config \
	&& ln -s /data/cache /home/spotify/.cache \
	&& ln -s /data/config /home/spotify/.config \
	&& chown -R spotify:spotify /data

USER spotify
WORKDIR /data

# PulseAudio server.
ENV PULSE_SERVER=/run/pulse/native

ENTRYPOINT ["/usr/bin/alltray", "/usr/bin/spotify"]
