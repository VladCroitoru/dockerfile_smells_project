FROM debian:jessie
MAINTAINER Jan Suchotzki <jan@inginform.de>

ENV VERSION_GCC 4.9

# Installiere die benötigten Anwendungen & Bibliotheken zur C-Entwicklung
RUN apt-get update && apt-get install -y --no-install-recommends \
		curl \
		ca-certificates \
		git \
		gcc-${VERSION_GCC} \
		libc6-dev \
		make \
		nano \
	&& rm -rf /var/lib/apt/lists/*
