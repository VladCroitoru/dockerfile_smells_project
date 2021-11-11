FROM debian:jessie
MAINTAINER  arctg70 <simon.zhou@gmail.com>

RUN apt-get update && \
    apt-get upgrade -y --force-yes &&\
    apt-get install -y strongswan libcharon-extra-plugins wget dnsutils iptables uuid-runtime kmod openssl


COPY ./run.sh /opt/src/run.sh
RUN chmod 755 /opt/src/run.sh

EXPOSE 500/udp 500/tcp 4500/udp 1701/udp 1723/tcp

VOLUME ["/lib/modules"]
VOLUME ["/data"]

CMD ["/opt/src/run.sh"]

