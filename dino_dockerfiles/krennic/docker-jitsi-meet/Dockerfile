FROM debian:latest
MAINTAINER Roberto Andrade <roberto@cloud.com>
ENV DEBIAN_FRONTEND noninteractive
ENV TERM xterm

RUN apt-get update && \
	apt-get install -y wget dnsutils vim telnet expect && \
	echo 'deb http://download.jitsi.org/nightly/deb unstable/' >> /etc/apt/sources.list && \
	wget -qO - https://download.jitsi.org/nightly/deb/unstable/archive.key | apt-key add - && \
	apt-get update && \
	apt-get -y install jitsi-meet && \
	apt-get clean

EXPOSE 80 443 5347
EXPOSE 10000/udp 10001/udp 10002/udp 10003/udp 10004/udp 10005/udp 10006/udp 10007/udp 10008/udp 10009/udp 10010/udp

COPY run.sh /run.sh
COPY autoconf.videobridge.exp /autoconf.videobridge.exp
COPY autoconf.jitsimeet.exp /autoconf.jitsimeet.exp

RUN chmod +x autoconf.videobridge.exp autoconf.jitsimeet.exp

CMD /run.sh