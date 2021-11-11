FROM ubuntu:14.04

MAINTAINER Tomohisa Kusano <siomiz@gmail.com>

RUN gpg --keyserver keyserver.ubuntu.com --recv-keys 249AD24C \
	&& gpg --export | apt-key add - \
	&& echo "deb http://ppa.launchpad.net/deluge-team/ppa/ubuntu trusty main" > /etc/apt/sources.list.d/deluge.list \
	&& apt-get update \
	&& apt-get install -y deluged deluge-web supervisor \
	&& useradd -m deluge \
	&& mkdir /opt/deluge-web.conf.d \
	&& chown deluge /var/log/supervisor /opt/deluge-web.conf.d

ADD supervisord.conf /etc/supervisor/

VOLUME ["/opt/deluge-web.conf.d"]

WORKDIR /home/deluge

USER deluge

EXPOSE 8112 58846

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]

