FROM paolodenti/jessie-jdk8:8.7

MAINTAINER Paolo Denti "paolo.denti@gmail.com"

# curl & wget
RUN DEBIAN_FRONTEND=noninteractive apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y wget curl

# openvpn 2.4
RUN DEBIAN_FRONTEND=noninteractive apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y net-tools iptables openssl
RUN DEBIAN_FRONTEND=noninteractive wget -nv -O - https://swupdate.openvpn.net/repos/repo-public.gpg | apt-key add -
RUN echo "deb http://build.openvpn.net/debian/openvpn/release/2.4 jessie main" > /etc/apt/sources.list.d/openvpn-aptrepo.list
RUN DEBIAN_FRONTEND=noninteractive apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y openvpn

# cleanup
RUN DEBIAN_FRONTEND=noninteractive apt-get purge -y wget && DEBIAN_FRONTEND=noninteractive apt-get -y autoremove
RUN rm -rf /var/lib/apt/lists/*
