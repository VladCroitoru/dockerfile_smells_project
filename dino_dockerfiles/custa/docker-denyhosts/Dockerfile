FROM alpine:latest
MAINTAINER custa <custa@126.com>

ENV REFRESHED_AT 2017-02-19

RUN apk update && apk add python

RUN apk add curl && \
	curl -OSL https://sourceforge.net/projects/denyhosts/files/denyhosts/2.6/DenyHosts-2.6.tar.gz && \
	apk del curl && \
	tar -zxvf DenyHosts-2.6.tar.gz && \
	cd DenyHosts-2.6 && python setup.py install && \
	cd / && rm -rf DenyHosts-2.6* && \
	ln -sf /usr/share/denyhosts/denyhosts.cfg-dist /usr/share/denyhosts/denyhosts.cfg && \
	ln -sf /usr/share/denyhosts/daemon-control-dist /usr/share/denyhosts/daemon-control && \
	mkdir -p /var/run/lock/subsys/

ADD run.sh /run.sh
RUN chmod +x /run.sh

ENTRYPOINT ["/run.sh"]
