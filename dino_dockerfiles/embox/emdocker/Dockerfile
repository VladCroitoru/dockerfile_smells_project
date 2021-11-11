
FROM ubuntu:16.04
MAINTAINER Anton Kozlov <drakon.mega@gmail.com>

# Container utils
RUN apt-get update && \
	DEBIAN_FRONTEND=noninteractive apt-get -y --no-install-recommends install \
		sudo \
		iptables \
		openssh-server \
		iproute2 \
		bzip2 \
		unzip \
		xz-utils \
		python \
		curl \
		make \
		patch \
		cpio \
		gcc-multilib \
		g++-multilib \
		gdb \
		qemu-system \
		ruby \
		bison \
		flex \
		bc \
		autoconf \
		pkg-config \
		mtd-utils \
		ntfs-3g \
		autotools-dev \
		automake \
		xutils-dev \
		libtool && \
	apt-get clean && \
	rm -rf /var/lib/apt /var/cache/apt

## arm crosscompiler
## NOTE use insecure connection (-k) to avoid troubles with outdated local certificates
## another option is to update certificates (i.e. from https://curl.haxx.se/docs/caextract.html) and provide the file with --cacert
RUN curl -k -L "https://developer.arm.com/-/media/Files/downloads/gnu-rm/6-2017q2/gcc-arm-none-eabi-6-2017-q2-update-linux.tar.bz2" | \
	tar -jxC /opt

## aarch64 crosscompiler
RUN curl -k -L "https://developer.arm.com/-/media/Files/downloads/gnu-a/8.3-2019.03/binrel/gcc-arm-8.3-2019.03-x86_64-aarch64-elf.tar.xz" | \
	tar -xJC /opt

## other crosscompilers
RUN for a in microblaze mips powerpc sparc; do \
	curl -k -L "https://github.com/embox/crosstool/releases/download/2.28-6.3.0-7.12/$a-elf-toolchain.tar.bz2" | \
		tar -jxC /opt; \
	done

ENV PATH=$PATH:\
/opt/gcc-arm-none-eabi-6-2017-q2-update/bin:\
/opt/gcc-arm-8.3-2019.03-x86_64-aarch64-elf/bin:\
/opt/microblaze-elf-toolchain/bin:\
/opt/mips-elf-toolchain/bin:\
/opt/powerpc-elf-toolchain/bin:\
/opt/sparc-elf-toolchain/bin

COPY create_matching_user.sh /usr/local/sbin/
COPY docker_start.sh /usr/local/sbin/

COPY id_rsa.pub /home/user/.ssh/authorized_keys
COPY user.bashrc /home/user/.bashrc
COPY user.bash_profile /home/user/.bash_profile
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

## x86/test/fs
RUN for i in $(seq 0 9); do \
		mknod /dev/loop$i -m0660 b 7 $i; \
	done

EXPOSE 22
VOLUME /embox
CMD ["/usr/local/sbin/docker_start.sh"]
