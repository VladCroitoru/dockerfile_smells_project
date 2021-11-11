FROM debian:wheezy

MAINTAINER Tomohisa Kusano <siomiz@gmail.com>

RUN apt-get update \
	&& DEBIAN_FRONTEND=noninteractive apt-get install -y wget

WORKDIR /opt/btsync

RUN wget -qO- http://download.getsyncapp.com/endpoint/btsync/os/linux-x64/track/stable | tar zxv

RUN DEBIAN_FRONTEND=noninteractive apt-get purge -y wget \
	&& DEBIAN_FRONTEND=noninteractive apt-get clean

VOLUME ["/media/storage", "/opt/btsync/.sync"]

RUN ./btsync --dump-sample-config > sync.conf \
	&& sed -ri '/"device_name"/s/"My Sync Device"/"'"${HOSTNAME}"'"/;' sync.conf \
	&& sed -ri '/"use_upnp"/s/true/false/;' sync.conf \
	&& sed -ri '/"listening_port"/s/0,/18888,/;' sync.conf \
	&& sed -ri '/"directory_root"/s/\/\///;' sync.conf \
	&& sed -ri '/"directory_root"/s#: ?"(.*)"#: "/media/storage"#;' sync.conf

EXPOSE 8888 18888

CMD ["/opt/btsync/btsync", "--config", "sync.conf", "--nodaemon"]
