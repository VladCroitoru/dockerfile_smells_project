FROM ubuntu:14.04
MAINTAINER Artur Mudrykh <arturmon82@gmail.com>

ARG VCS_REF
ARG BUILD_DATE
ARG BRANCH_NAME

LABEL org.label-schema.vcs-ref=$VCS_REF \
	org.label-schema.vcs-url="https://github.com/domoticz/domoticz" \
	org.label-schema.url="https://domoticz.com/" \
	org.label-schema.name="Domoticz" \
	org.label-schema.docker.dockerfile="/Dockerfile" \
	org.label-schema.license="GPLv3" \
	org.label-schema.build-date=$BUILD_DATE



## packages dependencies
RUN apt-get update \
	&& apt-get install -y \
	wget \
	libboost-thread1.55-dev libssl-dev libcurl4-openssl-dev libusb-dev python3-dev \
	&& rm -rf /var/lib/apt/lists/*

## Domoticz installation
RUN mkdir -p /opt/domoticz \
	&& wget -qO- http://releases.domoticz.com/releases/release/domoticz_linux_x86_64.tgz | tar xz -C /opt/domoticz

WORKDIR /opt/domoticz

RUN mkdir -p /opt/domoticz/backup  /scripts
VOLUME ["/opt/domoticz/scripts", "/opt/domoticz/backups",  "/config"]

EXPOSE 8080 443 6144 9898

ENTRYPOINT ["/opt/domoticz/domoticz", "-dbase", "/config/domoticz.db", "-log", "/config/domoticz.log"]
CMD ["-www", "8080"]
