FROM centos:centos6

MAINTAINER coleman <coleman_dlut@hotmail.com>

ENV VERSION v4.17-9562-beta-2015.05.30
ENV RADIUS_SERVER=
ENV RADIUS_SECRET=
ENV CERT_FILE=
ENV CERT_KEY=
WORKDIR /usr/local/vpnserver

RUN yum -y update && \
        yum -y install gcc binutils tar gzip glibc zlib openssl readline ncurses wget && \
        wget http://jp.softether-download.com/files/softether/${VERSION}-tree/Linux/SoftEther_VPN_Server/64bit_-_Intel_x64_or_AMD64/softether-vpnserver-${VERSION}-linux-x64-64bit.tar.gz -O /tmp/softether-vpnserver.tar.gz && \
        tar -xzvf /tmp/softether-vpnserver.tar.gz -C /usr/local/ && \
        rm -f /tmp/softether-vpnserver.tar.gz && \
        make i_read_and_agree_the_license_agreement && \
        yum -y erase gcc tar wget cloog-ppl cpp glibc-devel glibc-headers kernel-headers libgomp mpfr ppl && \
        yum clean all

EXPOSE 443/tcp 992/tcp 1194/tcp 1194/udp 5555/tcp 500/udp 4500/udp

# Run
ADD run.sh /opt/run.sh
RUN chmod 700 /opt/run.sh

CMD /opt/run.sh

