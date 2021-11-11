FROM phusion/baseimage
MAINTAINER arr0n 

RUN apt-get update && apt-get install -y \
	curl 

ADD etcinitdpixelserv.sh /etc/init.d/pixelserv
RUN	chmod 755 /etc/init.d/pixelserv

RUN cd /usr/local/bin/ && \
	curl http://proxytunnel.sourceforge.net/files/pixelserv.pl.txt > pixelserv && \
	chmod 755 pixelserv

RUN update-rc.d pixelserv defaults

RUN apt-get clean

RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

EXPOSE 80

CMD ["/usr/local/bin/pixelserv", "&"]
