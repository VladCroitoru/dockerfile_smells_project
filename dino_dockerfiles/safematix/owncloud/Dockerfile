FROM owncloud:8.2.1

MAINTAINER Robert Ressl <r.ressl@safematix.com>

RUN apt-get update && \
	apt-get install -y libreoffice sudo && \
	apt-get clean autoclean && \
	apt-get autoremove --yes && \
	rm -rf /var/cache/{apt,dpkg,cache,log} && \
	rm -rf /var/lib/{apt,dpkg,cache,log}
