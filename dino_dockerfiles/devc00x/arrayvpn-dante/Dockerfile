FROM ubuntu:16.04
ADD scripts/ArrayNetworksL3VPN_LINUX.bin /root

RUN dpkg --add-architecture i386 && apt-get update && apt-get install -y bzip2 kmod libstdc++5:i386 libpam0g:i386 libx11-6:i386 expect iptables net-tools iputils-ping dante-server iproute2 zlib1g:i386

RUN cd /root && bash -x ArrayNetworksL3VPN_LINUX.bin

ADD scripts/array.sh /root
RUN chmod +x /root/array.sh

ADD scripts/danted.conf /etc/danted.conf

EXPOSE 1088

CMD ["/root/array.sh"]
