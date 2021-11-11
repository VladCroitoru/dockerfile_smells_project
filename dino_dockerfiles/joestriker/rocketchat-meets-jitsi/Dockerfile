FROM rocketchat/base
ENV RC_JITSI_VERSION latest
MAINTAINER buildmaster@rocket.chat

RUN apt-get update && \
        apt-get install -y wget dnsutils vim telnet && \
        echo 'deb http://download.jitsi.org/nightly/deb unstable/' >> /etc/apt/sources.list && \
        wget -qO - https://download.jitsi.org/nightly/deb/unstable/archive.key | apt-key add - && \
        apt-get update && \
        apt-get -y install jitsi-meet && \
        apt-get clean

EXPOSE 80 443 5347
EXPOSE 10000/udp 10001/udp 10002/udp 10003/udp 10004/udp 10005/udp 10006/udp 10007/udp 10008/udp 10009/udp 10010/udp


COPY start-jitsi.sh /usr/bin/
RUN chmod +x /usr/bin/start-jitsi.sh
CMD ["usr/bin/start-jitsi.sh"]
