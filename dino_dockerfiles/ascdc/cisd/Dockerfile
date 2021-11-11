FROM ubuntu:trusty
MAINTAINER ASCDC <asdc.sinica@gmail.com>

ADD run.sh /script/run.sh

RUN DEBIAN_FRONTEND=noninteractive && \
	chmod +x /script/*.sh && \
	apt-get update && \
	apt-get -y dist-upgrade && \
	locale-gen en_US.UTF-8 && \
	export LANG=en_US.UTF-8 && \
	apt-get -y install gcc make automake perl libgdk-pixbuf2.0-dev libaio1 libaio-dev wget

EXPOSE 80
WORKDIR /script
ENTRYPOINT ["/script/run.sh"]
