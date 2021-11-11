FROM debian:stable-slim
LABEL maintainer="Jean-Avit Promis docker@katagena.com"

LABEL org.label-schema.vcs-url="https://github.com/nouchka/docker-signal"
LABEL version="latest"

ARG PUID=1000
ARG PGID=1000
ENV PUID ${PUID}
ENV PGID ${PGID}

ARG VERSION=5
## LATEST_RELEASE=v5.18.0

WORKDIR /tmp
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN apt-get update && \
	DEBIAN_FRONTEND=noninteractive apt-get -yq --no-install-recommends install wget=* tar=* ca-certificates=* gnupg=* && \
	wget -O- https://updates.signal.org/desktop/apt/keys.asc | apt-key add - && \
	echo 'deb [arch=amd64] https://updates.signal.org/desktop/apt xenial main' >/etc/apt/sources.list.d/signal-xenial.list && \
	apt-get update && \
	apt-get install -y signal-desktop=${VERSION}.* libx11-xcb1=* libxshmfence1=* libdrm2=* libgbm1=* && \
	chmod +x /usr/bin/signal-desktop && \
	rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
	export uid=${PUID} gid=${PGID} && \
	mkdir -p /home/developer && \
	echo "developer:x:${uid}:${gid}:Developer,,,:/home/developer:/bin/bash" >> /etc/passwd && \
	echo "developer:x:${uid}:" >> /etc/group && \
	chown "${uid}:${gid}" -R /home/developer

VOLUME /home/developer/.config/Signal
WORKDIR /home/developer/

USER developer
ENTRYPOINT [ "/usr/bin/signal-desktop" ]
CMD [ "--no-sandbox" ]
