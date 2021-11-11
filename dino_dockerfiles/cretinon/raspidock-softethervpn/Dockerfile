FROM resin/rpi-raspbian

RUN [ "cross-build-start"] 

RUN apt-get update  && apt-get upgrade

WORKDIR /usr/local/vpnserver

RUN apt-get update &&\
        apt-get -y -q install iptables vim isc-dhcp-relay net-tools tcpdump iputils-ping gcc make wget build-essential && \
        apt-get clean && \
        rm -rf /var/cache/apt/* /var/lib/apt/lists/*
RUN wget http://www.softether-download.com/files/softether/v4.20-9608-rtm-2016.04.17-tree/Linux/SoftEther_VPN_Server/32bit_-_ARM_EABI/softether-vpnserver-v4.20-9608-rtm-2016.04.17-linux-arm_eabi-32bit.tar.gz -O /tmp/softether-vpnserver.tar.gz &&\
        tar -xzvf /tmp/softether-vpnserver.tar.gz -C /usr/local/ &&\
        rm /tmp/softether-vpnserver.tar.gz &&\
        make i_read_and_agree_the_license_agreement &&\
        apt-get purge -y -q --auto-remove gcc make wget
ADD runner.sh /usr/local/vpnserver/runner.sh
RUN chmod 755 /usr/local/vpnserver/runner.sh

EXPOSE 991/tcp 443/tcp 992/tcp 1194/tcp 1194/udp 5555/tcp 500/udp 4500/udp
ENTRYPOINT ["/usr/local/vpnserver/runner.sh"]

RUN [ "cross-build-end" ]  
