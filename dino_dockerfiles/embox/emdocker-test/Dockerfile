
FROM embox/emdocker as build

RUN apt-get update && \
	DEBIAN_FRONTEND=noninteractive apt-get -y --no-install-recommends install \
		nfs-kernel-server \
		nfs-common \
		samba \
		mkisofs \
		net-tools \
		isc-dhcp-server \
		iputils-ping \
		telnet \
		ntp \
		openbsd-inetd \
		psmisc \
		wget \
		expect \
		snmp \
		xvfb \
		xvnc4viewer \
		ffmpeg \
		git \
		dosfstools && \
	apt-get clean && \
	rm -rf /var/lib/apt /var/cache/apt

# x86/test/fs nfs
RUN mkdir -p -m 777 /var/nfs_test
COPY exports /etc/

# x86/test/fs cifs
RUN mkdir -p -m 777 /var/cifs_test
COPY smb.conf /etc/samba/

# x86/test/net
COPY dhcpd.conf /etc/dhcp/
COPY isc-dhcp-server /etc/default/
COPY ntp.conf /etc/
RUN useradd -u 65534 -o -ms /bin/bash rlogin_user
RUN /bin/echo -e "rlogin\nrlogin" | passwd rlogin_user

FROM scratch
MAINTAINER Anton Kozlov <drakon.mega@gmail.com>

COPY --from=build / /

ENV PATH=$PATH:\
/opt/gcc-arm-none-eabi-6-2017-q2-update/bin:\
/opt/gcc-arm-8.3-2019.03-x86_64-aarch64-elf/bin:\
/opt/microblaze-elf-toolchain/bin:\
/opt/mips-elf-toolchain/bin:\
/opt/powerpc-elf-toolchain/bin:\
/opt/sparc-elf-toolchain/bin

CMD mount -t tmpfs none /var/nfs_test && \
	service rpcbind restart && \
	/etc/init.d/nfs-kernel-server restart && \
	/etc/init.d/nmbd restart && \
	/etc/init.d/smbd restart && \
	/etc/init.d/ntp restart && \
	inetd && \
	/usr/local/sbin/docker_start.sh


