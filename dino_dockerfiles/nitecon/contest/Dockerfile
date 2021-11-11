FROM debian:stable

RUN apt-get update && apt-get install -y --no-install-recommends \
		ca-certificates \
		curl \
		wget \
		dnsutils \
		netcat \
		traceroute \
	&& rm -rf /var/lib/apt/lists/* \
	&& chsh -s /bin/bash

RUN set -ex; \
	if ! command -v gpg > /dev/null; then \
		apt-get update; \
		apt-get install -y --no-install-recommends \
			gnupg2 \
			dirmngr \
		; \
		rm -rf /var/lib/apt/lists/*; \
fi

ENTRYPOINT while true; do sleep 10000; done
