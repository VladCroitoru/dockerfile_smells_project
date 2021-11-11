FROM ubuntu:17.10

RUN apt update && DEBIAN_FRONTEND=noninteractive apt dist-upgrade -y --no-install-recommends --fix-missing && \
	DEBIAN_FRONTEND=noninteractive apt install -y --no-install-recommends context context-doc-nonfree context-modules context-nonfree && \
	DEBIAN_FRONTEND=noninteractive apt autoremove -y && \
	rm -rf \
		/var/lib/apt/lists/* \
		/tmp/* \
		/var/tmp/*

