FROM centos:latest
MAINTAINER "kev" spam4kev@gmail.com

EXPOSE 53 53/tcp 67 68/udp 69/udp 69 4011/udp
#RUN yum update
RUN yum install -y wget \
		   tftp-server \
		   iproute \
		   iptables-services \
		   dnsmasq && \
    mkdir /tftpboot
COPY ./pxe-entrypoint.sh /tmp/pxe-entrypoint.sh
COPY ./pxe-entrypoint-razor.sh /tmp/pxe-entrypoint-razor.sh
RUN chmod +x /tmp/pxe-entrypoint*
WORKDIR /tftpboot
CMD \
    wget --tries=0 http://10.11.11.59:8150/api/microkernel/bootstrap -O /tftpboot/bootstrap.ipxe && \
    wget --tries=0 http://boot.ipxe.org/undionly.kpxe && \
    chmod +x /tftpboot/* && \
    dnsmasq  \
		--dhcp-match=IPXEBOOT,175 \
		--enable-tftp \
		--dhcp-range=10.11.11.0,static \
	        --dhcp-host=c8:60:00:de:ba:76,10.11.11.201 \
		--tftp-root=/tftpboot \
		--dhcp-boot=net:IPXEBOOT,bootstrap.ipxe \
		--dhcp-boot=undionly.kpxe \
		--log-dhcp \
		--no-daemon
#		--dhcp-range=10.11.11.201,10.11.11.202,1h \
#		--dhcp-range=$mySUBNET.201,$mySUBNET.202,255.255.255.0,1h \
#		--bind-dynamic \
