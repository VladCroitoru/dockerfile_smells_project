# ARK Server Container for Titan Server

FROM cm2network/steamcmd:root
LABEL maintainer="m.d.mcnamara@gmail.com"
LABEL description="ARK Server Container for Titan Server"

ARG PACKAGES_TO_INSTALL="procps zip rsync"

RUN apt-get update \
    && apt-get install -y ${PACKAGES_TO_INSTALL} \
	&& apt-get clean autoclean \
	&& apt-get autoremove -y \
	&& rm -rf /var/lib/apt/lists/*

COPY controlARK.bash /controlARK.bash

USER steam